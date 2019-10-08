function opendiv() {
    document.getElementById('light').style.display = 'block';
    document.getElementById('fade').style.display = 'block';
}
function closediv() {
    document.getElementById('light').style.display = 'none';
    document.getElementById('fade').style.display = 'none';
}

function emptyInput() {
    document.getElementById("prompt").innerHTML = '';
}
//新增用例
$(function () {
    $("#level").change(function () {
        if ($("#level").find("option:selected").text() === '否') {
            $('input[name="softId"]').attr("readonly", true);
        } else {
            $('input[name="softId"]').removeAttr("readonly");
        }
    });
});

//新增用例
$(function () {
    $("#submit").click(function () {
        const $name = $('input[name="caseName"]').val().length;
        const $number = $('input[name="number"]').val().length;
        const $softtime = $('input[name="softTime"]').val().length;
        const $assercontent = $('input[name="rebate"]').val().length;
        const $flag = $number !== 0 && $name !== 0 && $softtime !== 0 && $assercontent !== 0;
        if (!$flag) {
            alert("存在用例名称、下载次数、上传时间、预期结果为空！")
        } else {
            $.ajax(
                {
                    type: "POST",
                    url: '/download/caseManner/',
                    data: $("#form").serialize(),
                    async: true,
                    error: function (respose) {
                        alert(respose);
                        return false;
                    },
                    success: function (respose) {
                        alert(respose);
                        window.location.href = '/download/case/'+$("input[name='project']").val()
                    }
                });
        }

    });
});

//检查用例编号是否重复
function check() {
    const caseId = $("input[name='caseId']").val();
    $.ajax(
        {
            type: "POST",
            url: "/download/check/",
            dataType: "json",
            data: {data: {"caseId": caseId}},
            async: false,
            error: function (repose) {
                alert(repose.content);
                $("#prompt").html(repose.result)
            },
            success: function (respose) {
                $("#prompt").html(respose.result)
            }
        });
}
//执行用例，提交选择的用例提交到后台进行测试
function submitcase() {
    const $ids = [];
    const $carbons = $("#list-table").find('input:checked');
    if ($carbons.length === 0) {
        alert("请最少选择一条用例！");
        return false;
    } else {
    }
    $($carbons).each(function () {
        $ids.push($(this).attr('data-id'));   //找到对应checkbox中data-id属性值，然后push给空数组$ids
    });
    const $caseid = $ids.join(',');              //将数组转化为用逗号隔开的字符串
    const btn = confirm("确定执行用例吗？");
    if (btn) {
        //通过ajax提交数据到后台
        $.ajax(
            {
                type: "POST",
                url: "/download/startTestCase/",
                dataType: "json",
                data: {data: {"caseId": $caseid}},
                async: true,
                error: function (respose) {
                    alert(respose.result);
                },
                success: function (respose) {
                    alert(respose.result);
                }
            });
    }
}
//执行所有用例
$(function () {
    $("#all").click(function () {
        const btn = confirm("确定执行全部用例吗？");
        if (btn) {
            //通过ajax提交数据到后台
            $.ajax(
                {
                    type: "POST",
                    url: "/download/startTestCase/",
                    dataType: "json",
                    data: {data: {"caseId": 'all',"project":$("#all").attr("project")}},
                    async: false,
                    error: function (respose) {
                        alert(respose.result);
                    },
                    success: function (respose) {
                        alert(respose.result);
                    }
                });
        }
    });
});

//多线程写数据
$(function () {
    $("#allthread").click(function () {
        const btn = confirm("确定执行吗？");
        if (btn) {
            //通过ajax提交数据到后台
            $.ajax(
                {
                    type: "POST",
                    url: "/download/threadtest/",
                    dataType: "json",
                    data: {data: {"caserid": 'all'}},
                    async: false,
                    error: function (respose) {
                        alert(respose.result);
                    },
                    success: function (respose) {
                        alert(respose.result);
                    }
                });
        }
    });
});

//多线程获取结果
$(function () {
    $("#threadGetResult").click(function () {
        const btn = confirm("确定使用多线程获取结果吗？");
        if (btn) {
            //通过ajax提交数据到后台
            $.ajax(
                {
                    type: "POST",
                    url: "/download/threadGetResult/",
                    dataType: "json",
                    data: {data: {"caserid": 'all'}},
                    async: false,
                    error: function (respose) {
                        alert(respose.result);
                    },
                    success: function (respose) {
                        alert(respose.result);
                    }
                });
        }
    });
});

//删除用例
$(function () {
    $(".del").click(function () {
        const $id = $(this).parents("td").prevAll(":eq(9)").text();
        console.log($id);
        const btn = confirm("确定删除该条用例吗？");
        if (btn) {
            //通过ajax提交数据到后台
            $.ajax(
                {
                    type: "POST",
                    url: "/download/deleteCase/",
                    dataType: "json",
                    data: {data: {"caserid": $id}},
                    async: false,
                    error: function (respose) {
                        alert(respose.content)
                    },
                    success: function () {
                        window.location.href = '/download/case/'+$("input[name='project']").val()
                    }
                });
        }
    });
});
//界面选择按钮操作
$(function () {

    //全选操作
    $(".Allcheck").click(function () {
        //获取属性名为name='checkbox'，然后添加checked= true，实现全选
        $("input[name='checkbox']").prop("checked", "true");
    });


    //获取属性名为name='checkbox'，删除所有checked属性
    $("#allnotcheck").click(function () {
        $("input[name='checkbox']").removeAttr("checked");
    });

    //反选
    // 添加全反选事件
    $("#btn3").click(function () {
        //获取属性名为name='checkbox'对其进行便利循环
        $("input[name='checkbox']").each(function () {
            //判断checked属性值，如果有则删除，如果没有则添加
            if ($(this).prop("checked")) {
                $(this).removeAttr("checked")
            } else {
                $(this).prop("checked", "true");
            }
        });
    });
});

$(function () {
    $("div .navbar-nav").find('li').click(function () {
        $(this).addClass("active").siblings("li").removeClass("active");
    });
});

//初始化环境
function initdata() {
    const btn = confirm("确定初始化环境吗？");
    if (btn) {
        //通过ajax提交数据到后台
        $.ajax(
            {
                type: "POST",
                url: "/download/initDate/",
                dataType: "json",
                data: {data: {}},
                async: false,
                error: function (data) {
                    alert(data.result)
                },
                success: function (data) {
                    alert(data.result);
                },
            });
    }
}
//修改用例
$(function () {
    $(".update").click(function () {
        //弹出修改模态框
        $("#update").show();
        $("#fade").show();

        //获取修改行数据
        const $arrMove = [];
        $(this).parent("td").siblings().each(function () {
            $arrMove.push($(this).text());
        });
        //赋值给模态框数据
        let func;
        if ($arrMove[1] === "返利") {
            func = "1";
        } else {
            func = "2";
        }
        //转换类型
        let type;
        if ($arrMove[5].split(":")[0] === "点数") {
            type = $arrMove[5].split(":")[1].split("")[0];
        } else if ($arrMove[5].split(":")[0] === "储值资料") {
            type = "6";
        } else if ($arrMove[5].split(":")[0] === "第三方") {
            type = "7";
        } else {
            type = "8";
        }
        console.log(type);
        //下载用户身份
        let authorType;
        if ($arrMove[11] === "初中高端网校通"){
            authorType = "20";
        }else if ($arrMove[11] === "初中中端网校通"){
            authorType = "21";
        }else if ($arrMove[11] === "初中普通网校通"){
            authorType = "22";
        }else if ($arrMove[11] === "高中高端网校通"){
            authorType = "23";
        }else if ($arrMove[11] === "高中中端网校通"){
            authorType = "24";
        }else {
            authorType = "25";
        }


        $("#func1").val(func);
        $("#caseid1").val($arrMove[2]);
        $("#casename1").val($arrMove[3]);
        $("#type1").val(type);
        $("#number1").val($arrMove[6]);
        $("#softid1").val($arrMove[4]);
        $("#softtime1").val($arrMove[7]);
        $("#softauthorid1").val($arrMove[8]);
        $("#assercontent1").val($arrMove[9]);
        $("#casenote1").val($arrMove[10]);
        $("#downloadID1").val(authorType);
    });
    //修改用例
    $("#updatabtn").click(function () {
        const $name = $('#casename1').val().length;
        const $id = $('#softid1').val().length;
        const $softtime = $('#softtime1').val().length;
        const $number = $('#number1').val().length;
        const $authorid = $('#softauthorid1').val().length;
        const $asser = $('#assercontent1').val().length;
        const $flag = $number !== 0 && $name !== 0 && $softtime !== 0 && $asser !== 0 && $id !== 0 && $authorid !== 0;
        if (!$flag) {
            $("#updateform input").each(function () {
                if (!$(this).val().length) {
                    $(this).css('borderColor', 'red');
                }
            });
            alert("存在用例名称、资料id、下载次数、上传时间、预期结果为空！")
        } else {
            $.ajax(
                {
                    type: "POST",
                    url: '/download/caseManner/',
                    data: $("#updateform").serialize(),
                    async: false,
                    error: function (data) {
                        alert(data.result);
                        return false;
                    },
                    success: function (data) {
                            alert(data);
                            if (data === "修改用例成功！"){
                               window.location.reload();
                            }
                    }
                });
        }

    });
    $("#updateform input").each(function () {
            $(this).click(function () {
                $(this).removeAttr('style', 'borderColor');
            });
        }
    );

    //取消修改
    $("#cancal").click(function () {
        $("#update").hide();
        $("#fade").hide();
        $("#updateform input").removeAttr('style', 'borderColor')
    });

});

//修改用例
$(function () {
    if ($("#level1").find("option:selected").text() === '否') {
        $('#softid1').attr("readonly", true);
    }
    $("#level1").change(function () {
        if ($("#level1").find("option:selected").text() === '否') {
            $('#softid1').attr("readonly", true);
        } else {
            $('#softid1').removeAttr("readonly");
        }
    });
});

$(function () {
   $("#name").html($.cookie('user'));
   $("#role").html($.cookie('userRoles'));
});
