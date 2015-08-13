$(function() {
    $("#fingerprint").click(function() {
        var url = "http://" + window.location.host + "/fingerprint";
        layer.open({
            type: 2,
            title: '',
            shadeClose: true,
            shade: false,
            maxmin: true, //开启最大化最小化按钮
            area: ['1800px', '1000px'],
            content: url
        });
    });
})