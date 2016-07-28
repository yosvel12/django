/**
 * Created by Yoan on 27/07/2016.
 */

function dologin(stormid) {

    //if ($("#dglogin").length == 0) {
    //    $("body").append("<div id='dglogin' style='display:none'></div>");
    //}
    //stormid = stormid || 0;
    //try {
    //    $.ajax({
    //        url: "../login", data: "stormid=" + stormid, success: function (html) {
    //            $(".ui-dialog").css("display", "");
    //            $("#dglogin").html(html).css("display", "").dialog({
    //                title: "Login to Stormboard", width: 425, modal: true, beforeclose: function () {
    //                    $(this).dialog("destroy");
    //                }, close: function () {
    //                    $(this).dialog("destroy")
    //                }
    //            });
    //            $("#uname").focus();
    //        }, dataType: "html"
    //    });
    //} catch (e) {
    //    window.location = "users/login.html"
    //}
    window.location = "/login"
}


function dosignup() {
    $(".email-signup", "#dg_register").val("");
    $("#dg_register").dialog({title: "Signup", modal: true, width: 450, height: 375});
}


var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-79460-11']);
_gaq.push(['_setDomainName', 'stormboard.com']);
_gaq.push(['_trackPageview']);
(function () {
    var ga = document.createElement('script');
    ga.type = 'text/javascript';
    ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(ga, s);
})();
setTimeout(function () {
    var a = document.createElement("script");
    var b = document.getElementsByTagName("script")[0];
    a.src = document.location.protocol + "//dnn506yrbagrg.cloudfront.net/pages/scripts/0014/5357.js?" + Math.floor(new Date().getTime() / 3600000);
    a.async = true;
    a.type = "text/javascript";
    b.parentNode.insertBefore(a, b)
}, 1);
