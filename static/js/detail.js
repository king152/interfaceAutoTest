//判断结果为false显示红色,true显示为绿色
$(function () {
    $(".assert").each(function () {
        if ($(this).text() === 'False') {
            $(this).css({"color": "cornflowerblue", "backgroundColor": "red"});
        }
        else {
            $(this).css({"color": "cornflowerblue", "backgroundColor": "green"});
        }
    });
});
//获取选择的值
$(function () {
    $("#btn").click(function () {
        const btn = confirm("确定执行用例吗？");
        const $cased = $("#list-table").find('input:checked').attr('data-id');
        const $step = $(":checked").parents('td').next().find("option:selected").text();
        const $guid = $(":checked").parents('td').siblings();
        if ($("#list-table").find('input:checked').length === 0) {
            alert("请选择执行异常用例！");
            return false;
        } else {
        }
        if (btn) {
            //通过ajax提交数据到后台
            $.ajax(
                {
                    type: "POST",
                    url: "/download/stepTestCase/",
                    dataType: "json",
                    data: {data: {"data": $cased + ',' + $step}},
                    async: true,
                    error: function (respose) {
                        alert(respose.result);
                    },
                    success: function (respose) {
                        alert(respose.result);
                        window.location.reload();
                    }
                });
        }
    });
});

