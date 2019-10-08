//禁用启用操作
$(function () {
    $(".user_disable").click(function () {
        let $value;
        const $username = $(this).parents().prevAll("td:eq(4)").text();
        if ($(this).parents().prevAll("td:eq(1)").text() === "启用") {
            $value = "禁用";
        } else {
            $value = "启用";
        }
        const btn = confirm("确定" + $value + "当前用户吗？");
        if (btn) {
            $.ajax(
                {
                    type: "POST",
                    url: "/userinfo/user_operate/",
                    data: {"username": $username, "way": "disable", "value": $value},
                    async: false,
                    error: function (respose) {
                        alert(respose);
                    },
                    success: function () {
                        window.location.href = '/userinfo/user_list/'
                    }
                });
        } else {
        }

    });
});

//删除用户
$(function () {
    $(".user_delete").click(function () {
        const $username = $(this).parents().prevAll("td:eq(4)").text();
        const btn = confirm("确定删除当前用户吗？");
        if (btn) {
            $.ajax(
                {
                    type: "POST",
                    url: "/userinfo/user_operate/",
                    data: {"username": $username, "way": "delete"},
                    async: false,
                    error: function (respose) {
                        alert(respose);
                    },
                    success: function () {
                        window.location.href = '/userinfo/user_list/'
                    }
                });
        } else {
        }

    });
});

//重置资料ID
$(function () {
    $(".user_reset").click(function () {
        const $username = $(this).parents().prevAll("td:eq(4)").text();
        const btn = confirm("确定为当前用户重置资料id吗？");
        if (btn) {
            $.ajax(
                {
                    type: "POST",
                    url: "/userinfo/user_operate/",
                    data: {"username": $username, "way": "reset"},
                    async: false,
                    error: function (respose) {
                        alert(respose);
                    },
                    success: function () {
                        window.location.href = '/userinfo/user_list/'
                    }
                });
        } else {
        }

    });
});

//新增用户
$(function () {
    $(".newUser").click(function () {
        $(".whiteContent").css("display", "block");
        $(".black_overlay").css("display", "block");
        $(".user").val("");
        $(".email").val("");
    });

    $(".cancel_user").click(function () {
        $(".whiteContent").css("display", "none");
        $(".black_overlay").css("display", "none");
    });

    $(".newCreateUser").click(function () {
        $.ajax(
            {
                type: "POST",
                url: "/userinfo/user_operate/",
                data: $("#newUser_form").serialize(),
                async: false,
                error: function (respose) {
                    alert(respose);
                },
                success: function () {
                    window.location.href = '/userinfo/user_list/'
                }
            });
    });
});

//修改用户
$(function () {
    $(".user_update").click(function () {
        $(".updateContent").css("display", "block");
        $(".black_overlay").css("display", "block");
        $(".id").val($(this).parents().prevAll("td:eq(5)").text());
        $(".user").val($(this).parents().prevAll("td:eq(4)").text());
        $(".email").val($(this).parents().prevAll("td:eq(3)").text());
        $(".role").val($(this).parents().prevAll("td:eq(2)").text());
    });

    $(".cancel_user").click(function () {
        $(".updateContent").css("display", "none");
        $(".black_overlay").css("display", "none");
    });
    $(".updateUser").click(function () {
        $.ajax(
            {
                type: "POST",
                url: "/userinfo/user_operate/",
                data: $("#updateUser_form").serialize(),
                async: false,
                error: function (respose) {
                    alert(respose);
                },
                success: function () {
                    window.location.href = '/userinfo/user_list/'
                }
            });
    });
});

