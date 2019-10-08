$(function () {

    //验证用户名是否符合规范且是否已存在
    $(".user").blur(function () {
        if (!$(".user").val().length) {
            $(".user").css('borderColor', 'red');
            $("#u_tips").html("用户名不能为空！");
            $("#u_tips").attr("style", "color:red;");
            return false;
        }
        var $patrn = /^[a-zA-Z0-9]{5,24}$/;
        if (!$patrn.exec($(".user").val())) {
            $(".user").css('borderColor', 'red');
            $("#u_tips").html("用户名长度为5-24位，由大小写字母、数字组成！");
            $("#u_tips").attr("style", "color:red;");
            return false;
        } else {
            $(".user").css('borderColor', 'green');
            $("#u_tips").html("");
            $.ajax(
                {
                    type: "POST",
                    url: "/userinfo/check/",
                    data: {"username": $(".user").val()},
                    async: false,
                    error: function (respose) {
                        alert(respose);
                    },
                    success: function (respose) {
                        // $("#u_tips").removeAttr("style");
                        // $("#u_tips").html(respose);
                        if (respose == "用户名已存在,请重新输入!") {
                            $("#u_tips").html(respose);
                            $("#u_tips").removeAttr("style");
                            $("#u_tips").attr("style", "color:red;");
                            $(".user").css('borderColor', 'red');
                        }
                    }
                });
        }
    });

    //检查密码
    $(".pwd").blur(function () {
        var $patrn = /^(\w){6,18}$/;
        if (!$(".pwd").val()) {
            $(".pwd").css('borderColor', 'red');
            $("#p_tips").html("密码不能为空！");
            $("#p_tips").attr("style", "color:red;");
            return false;
        }
        if (!$patrn.exec($(".pwd").val())) {
            $(".pwd").css('borderColor', 'red');
            $("#p_tips").html("密码长度为6-18位，由字母、数字、下划线组成！");
            $("#p_tips").attr("style", "color:red;");
            return false;
        }
        $(".pwd").css('borderColor', 'green');
    });

    //检查确认密码
    $(".z_pwd").blur(function () {
        if (!($(".pwd").val() === $(".z_pwd").val())) {
            $(".z_pwd").css('borderColor', 'red');
            $("#zp_tips").html("确认密码与密码输入不一致！");
            $("#zp_tips").attr("style", "color:red;");
            return false;
        }
        $(".z_pwd").css('borderColor', 'green');
    });

    //检查邮箱
    $(".email").blur(function () {
        var $patrn = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/;
        if (!$(".email").val()) {
            $(".email").css('borderColor', 'red');
            $("#e_tips").html("邮箱不能为空！");
            $("#e_tips").attr("style", "color:red;");
            return false;
        }
        if (!$patrn.exec($(".email").val())) {
            $(".email").css('borderColor', 'red');
            $("#e_tips").html("邮箱格式不正确！");
            $("#e_tips").attr("style", "color:red;");
            return false;
        }
        $(".email").css('borderColor', 'green');
    });

    //验证输入框为空
    $(".reg_btn").click(function () {
        flag = true;
        $("#reg_form input").each(function () {
            if ($(this).val().length == 0) {
                $(this).css('borderColor', 'red');
                flag = false
            }
        });

        if (flag) {
            $.ajax(
                {
                    type: "POST",
                    url: "/userinfo/register/",
                    data: $("#reg_form").serialize(),
                    async: false,
                    error: function (respose) {
                        alert(respose);
                    },
                    success: function (respose) {
                        if (respose == "用户名已存在,请重新输入!") {
                            alert(respose);
                            return false;
                        }
                        if (respose == "注册成功,跳转到登录页面！") {
                            alert(respose);
                            location.href = "/userinfo/login/";
                        }
                    }
                });
        } else {
            alert("请将注册内容填写完整！");
        }
    });

    //判断鼠标点击输入框去掉红色提示
    $("#reg_form input").each(function () {
        $(this).click(function () {
            $(this).removeAttr('style', 'borderColor');
            $(this).next().html('');
        })
    });

});
