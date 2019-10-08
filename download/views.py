# -*- coding:utf-8 -*-
"""
@author:WangYong
@workNumber:xy04952
@fileName: views.py
@creatTime: 2019/08/05
"""
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage
from download.common.customPaginator import KingPaginator
from download.common.insertSql import requestdata, getSoftid_ordertime, initdownload
from download.models import CaseResult, TestSoftId, TestCase
from download.common.performCase import runCase, stepRunCase, runGetid, getResult
from download.common.UserCaseManner import caseOperate
from download.common.initEnvironment import initEnviron
from dateutil.parser import parse
import threading
import json
import time


# 初始化系统数据
def initDate(req):
    if req.method == "POST":
        threading.Thread(target=initEnviron).start()

        result = {'result': '初始化数据进行中！'}
        return HttpResponse(json.dumps(result))


# 首页
def index(request):
    if not request.session.get("username"):
        return redirect("login")
    else:
        role = request.COOKIES.get("userRoles")
        return render(request, 'index.html', {"role": role})


'''
 function:研一项目功能***start
'''


# 研一项目
def projectName(request):
    if not request.session.get("username"):
        return redirect("login")
    role = request.COOKIES.get("userRoles")
    return render(request, 'channel/rbcHome.html', {"role": role})


# 用例管理页面
def case(request, project):
    if not request.session.get("username"):
        return redirect("login")
    role = request.COOKIES.get("userRoles")
    username = request.session.get("username")
    caseList = TestCase.objects.filter(newCaseUser=username, project=project).order_by("-createTime")
    paginator = KingPaginator(caseList, 13)
    page = int(request.GET.get("page", 1))
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'channel/{}Case.html'.format(project), {"pages": pages, "role": role})


# 用例执行详情
def details(request, project):
    if not request.session.get("username"):
        return redirect("login")
    role = request.COOKIES.get("userRoles")
    typeName = ["高中高端网校通", "初中高端网校通"]
    case_list = CaseResult.objects.filter(executionUser=request.session.get("username"), project=project).order_by(
        '-executionTime')
    paginator = KingPaginator(case_list, 13)
    page = int(request.GET.get("page", 1))
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'channel/{}Detail.html'.format(project),
                  {"pages": pages, "role": role, "typeName": typeName})


# 记点通道报告
def report(request, project):
    if not request.session.get("username"):
        return redirect("login")
    role = request.COOKIES.get("userRoles")
    username = request.session.get("username")
    allCase = CaseResult.objects.filter(executionUser=username, project=project).count()
    failCase = CaseResult.objects.filter(assertResult=False, executionUser=username,
                                         project=project).count()
    successCase = CaseResult.objects.filter(assertResult=True, executionUser=username,
                                            project=project).count()
    return render(request, "channel/{}Report.html".format(project), {"all": allCase,
                                                                     "failed": failCase,
                                                                     "success": successCase,
                                                                     "role": role})


'''
 function:研一项目功能***end
'''


# 检查用例编号是否唯一
def check(request):
    if request.method == "POST":
        get_caseId = request.POST.get("data[caseId]")

        if len(get_caseId) == 0:
            result = {'result': '用例编号不能为空'}
            return HttpResponse(json.dumps(result))
        try:
            count = TestCase.objects.filter(caseId=get_caseId)
        except Exception as e:
            print(e)
            count = None
        if count:
            result = {'result': '用例编号已存在,请重新输入'}
            return HttpResponse(json.dumps(result))
        else:
            result = {'result': '可以使用'}
            return HttpResponse(json.dumps(result))


"""
00   "时间输入不合法！"
01   "存在用例编号、用例名称、下载次数、上传时间、预期结果为空！"
02   "新增用例成功！"
03   "资料下载量输入有误！"
04   "返利金额输入有误！"
05   "资料ID不能为空！"
06   "用例名称不能为空！"
07   "资料上传人不能为空！"
08   "修改用例成功！"
09   "资源ID已用完，请联系管理员再次分配！"
"""


# 用例新增、修改操作
def caseManner(request):
    user = request.session.get("username")
    if request.method == "POST":
        flag = caseOperate(request, user)
        if flag == "00":
            return HttpResponse("时间输入不合法！")
        elif flag == "01":
            return HttpResponse("存在用例编号、用例名称、下载次数、上传时间、预期结果为空！")
        elif flag == "02":
            return HttpResponse("新增用例成功！")
        elif flag == "03":
            return HttpResponse("资料下载量输入有误！")
        elif flag == "04":
            return HttpResponse("返利金额输入有误！")
        elif flag == "05":
            return HttpResponse("资料ID不能为空！")
        elif flag == "06":
            return HttpResponse("用例名称不能为空！")
        elif flag == "07":
            return HttpResponse("资料上传人不能为空！")
        elif flag == "08":
            return HttpResponse("修改用例成功！")
        else:
            return HttpResponse("资料softID已用完，请联系管理员分配！")


# 删除用例
def deleteCase(req):
    if req.method == "POST":
        get_caseId = req.POST.get("data[caserid]")
        try:
            count = TestCase.objects.filter(caseId=get_caseId).delete()
        except Exception as e:
            print(e)
            count = None
        if count:
            result = {'result': '用例删除成功！'}
            return HttpResponse(json.dumps(result))
        else:
            result = {'result': '删除失败，服务器出现异常！'}
            return HttpResponse(json.dumps(result))


# 执行用例
def startTestCase(request):
    if request.method == "POST":
        ids = request.POST.get("data[caseId]")
        project = request.POST.get("data[project]")
        username = request.session.get("username")

        # 开启一个线程去执行用例
        threading.Thread(target=runCase, args=(ids, username, project,)).start()

        # 返回信息给前端
        result = {'result': '提交用例执行操作成功！'}
        return HttpResponse(json.dumps(result))


# 步骤化执行用例功能
def stepTestCase(req):
    if req.method == "POST":
        data = req.POST.get("data[data]").split(',')
        caseId = data[0]
        step = data[1]
        print(caseId, step)
        # 开启一个线程运行
        threading.Thread(target=stepRunCase, args=(step, caseId,)).start()

        result = {'result': '用例执行中....'}
        return HttpResponse(json.dumps(result))


# 工具页
def tools(req):
    return render(req, "tools.html")


# 抽奖功能
def luckydraw(req):
    if req.method == "POST":
        userId = req.POST.get("userid")
        number = req.POST.get("number")
        startTime = parse(req.POST.get("starttime"))
        endTime = parse(req.POST.get("endtime"))
        if len(userId) == 0:
            return HttpResponse("用户id不能为空！")
        solids = getSoftid_ordertime(int(number), startTime, endTime)
        for sifted in solids:
            initdownload(sifted[0], userId)
        time.sleep(5)
        for sifted in solids:
            requestdata(userId, sifted[0])
    return HttpResponse("抽奖完成！")


def threadtest(req):
    if req.method == "POST":
        lock = threading.Lock()
        threads = []  # 初始化线程列表
        number = int(TestSoftId.objects.all().count() / 10)  # 获取总数并分成10片
        started = TestSoftId.objects.all().first().id  # 获取初始位置id
        for i in range(10):
            if i < 9:  # 得到每片最后一个id
                ended = started + number
            else:  # 最后一片拿到最后一个id
                ended = TestSoftId.objects.all().last().id
            t = threading.Thread(target=runGetid, args=(lock, started, ended,))  # 初始化线程
            threads.append(t)  # 将线程加入threads组
            started += number  # 得到每片初始id
        for j in threads:  # 开始运行线程
            j.start()

        result = {'result': '多线程执行中....'}
        return HttpResponse(json.dumps(result))


def threadGetResult(req):
    if req.started == "POST":
        lock = threading.Lock()
        threads = []  # 初始化线程列表
        number = int(TestSoftId.objects.all().count() / 10)  # 获取总数并分成10片
        started = TestSoftId.objects.all().first().id  # h获取初始位置id
        for i in range(10):
            if i < 9:  # 得到每片最后一个id
                ended = started + number
            else:  # 最后一片拿到最后一个id
                ended = TestSoftId.objects.all().last().id
            t = threading.Thread(target=getResult, args=(lock, started, ended,))  # 初始化线程
            threads.append(t)  # 将线程加入threads组
            started += number  # 得到每片初始id
        for j in threads:  # 开始运行线程
            j.start()

        result = {'result': '多线程执行中....'}
        return HttpResponse(json.dumps(result))
