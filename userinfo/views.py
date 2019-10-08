from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse

from download.common.customPaginator import KingPaginator
from userinfo.common.tools import *
from Logs.log import get_log
from userinfo.common.userinit import *
from .models import User
import re
import threading
import time

log = get_log("login")


# 登录页面
def login(request):
    if request.session.get("username"):
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")

        try:
            count = User.objects.filter(username=username)
        except Exception as e:
            log.info("登录用户查询异常：", e)
            count = None
        if not count:
            return render(request, 'user/login.html', {"massage": "账号密码输入错误！"})

        try:
            res = User.objects.filter(username=username, userState=False)
        except Exception as e:
            log.info("登录用户查询异常：", e)
            res = None
        if res:
            return render(request, 'user/login.html', {"massage": "账号已被禁用，请联系管理员！"})

        res = User.objects.filter(username=username).values()
        if pwd == decrypt(res[0]["password"]):
            responses = redirect("index")
            request.session["username"] = username
            responses.set_cookie("user", username)
            responses.set_cookie("userRoles", res[0]["username_role"])
            request.session.setdefault('username', username)
            return responses
        else:
            return render(request, 'user/login.html', {"massage": "账号密码输入错误！"})
    return render(request, 'user/login.html')


# 注册
def register(request):
    if request.method == "POST":
        u_name = request.POST.get("username")
        u_pwd = request.POST.get("pwd")
        u_email = request.POST.get("email")
        if len(u_name) == 0 or len(u_email) == 0 or len(u_pwd) == 0:
            return HttpResponse("用户名、密码、邮箱不能为空11！")

        if not len(re.findall(r'^\w{5,20}$', u_name)):
            return HttpResponse("用户名长度为5-24位，由大小写字母、数字组成！")

        if not len(re.findall(r'^\w{6,18}$', u_pwd)):
            return HttpResponse("密码长度为6-18位，由字母、数字、下划线组成！")

        if not len(re.findall(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', u_email)):
            return HttpResponse("邮箱格式不正确！")

        try:
            count = User.objects.filter(username=u_name)
        except Exception as e:
            log.info("注册用户名查询异常：", e)
            count = None
        if count:
            return HttpResponse('用户名已存在,请重新输入!')

        threading.Thread(target=initUserSoftId, args=(u_name,)).start()

        User.objects.create(username=u_name, password=encrypt(u_pwd), email=u_email, username_role='Averaged',
                            regTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                            userState=True)
        return HttpResponse("注册成功,跳转到登录页面！")
    return render(request, 'user/register.html')


# 退出
def logout(request):
    request.session.flush()
    return redirect("login")


# 检查用户名是否重复
def check(request):
    if request.method == "POST":
        u_name = request.POST.get("username")

        if len(u_name) == 0:
            return HttpResponse('用户名不能为空！')
        if len(u_name) < 6 or len(u_name) > 24:
            return HttpResponse('用户名长度为6-24位字符之间！')
        try:
            count = User.objects.filter(username=u_name)
        except Exception as e:
            log.info("注册用户名查询异常：", e)
            count = None
        if count:
            return HttpResponse('用户名已存在,请重新输入!')
        else:
            return HttpResponse('用户名可以使用！')


'''
角色：
1、管理员 Administrator
2、测试人员 testers
3、开发人员 developers
4、产品人员 product
5、普通用户 averaged
'''


# 用户管理
def user_list(request):
    if not request.session.get("username"):
        return redirect("login")
    role = request.COOKIES.get("userRoles")
    if role != "Administrator":
        return render(request, "permiss.html", {"role": role})
    userList = User.objects.all().order_by("id")
    paginator = KingPaginator(userList, 10)
    page = int(request.GET.get("page", 1))
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, "user/userlist.html", {"pages": pages, "role": role})


# 用户操作 增、删、改、禁用、重置
def user_operate(request):
    if request.method == "POST":
        u_name = request.POST.get("username")
        if request.POST.get("way") == "disable":
            value = request.POST.get("value")
            if value == "启用":
                state = True
            else:
                state = False
            User.objects.filter(username=u_name).update(userState=state)
            return HttpResponse("禁用成功！")
        elif request.POST.get("way") == "delete":
            User.objects.filter(username=u_name).delete()
            return HttpResponse("删除成功！")
        elif request.POST.get("way") == "reset":
            threading.Thread(target=initUserSoftId, args=(u_name,)).start()
            return HttpResponse("重置成功！")
        elif request.POST.get("way") == "new":
            u_pwd = request.POST.get("pwd")
            u_email = request.POST.get("email")
            u_role = request.POST.get("role")
            User.objects.create(username=u_name, password=encrypt(u_pwd), email=u_email, username_role=u_role,
                                regTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                                userState=True)
            return HttpResponse("新增成功！")
        elif request.POST.get("way") == "update":
            u_id = request.POST.get("id")
            u_pwd = request.POST.get("pwd")
            u_email = request.POST.get("email")
            u_role = request.POST.get("role")
            if len(u_pwd) == 0:
                User.objects.filter(id=u_id).update(username=u_name, email=u_email, username_role=u_role)
            else:
                User.objects.filter(id=u_id).update(username=u_name, password=encrypt(u_pwd), email=u_email,
                                                    username_role=u_role)
            return HttpResponse("修改成功！")
        else:
            return HttpResponse("传参错误！")
