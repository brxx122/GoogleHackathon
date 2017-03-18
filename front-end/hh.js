console.log("========================");
var htmlobj=$.ajax({url:"header.html",async:false});
$("#common-header").prepend(htmlobj.responseText);
console.log(htmlobj.responseText);
var page = 0;
var current_news=0;
var J = [{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck2","author":"hh1","time":"2017年2月21日"},
{"title":"fuck2","author":"hh1","time":"2017年2月21日"},
{"title":"fuck2","author":"hh1","time":"2017年2月21日"},
{"title":"fuck2","author":"hh1","time":"2017年2月21日"},
{"title":"fuck2","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},
{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"}];
var get_labels = function(){
    $.get("url...").done
}
var copy_right = function () {
    if (current_news <= 5) {return false;}
    $.post("{{url_for('hello')}}", page++, success(data));
};  
var copy_left = function () {
    if (page==0) {return false;}
    $.post("{{url_for('hello')}}", page--, success(data));
}; 

$(".previous").click(copy_left()); 
$(".next").click(copy_right());

var success = function(data) {
    current_news=0;
    console.log("loading...");
    data = eval(data);
    console.log("length:"+data.length);
    var result = ""
    $.each(data,function(i,item){
        if (i == 5) {return false;}
        current_news++;
        var title = item.title;
        var author = item.author;
        var time = item.time;
        var content = item.title;

        var str =  '<article id=73 class="post">\
        <div class="post-head">\
        <h1 id="title" class="post-title"><a href="post.html">'+title+'</a></h1>\
        <div class="post-meta">\
        <span class="author">作者：<a id="author" href="personal.html">'+author+'</a></span> &emsp;&bull;\
        <span time id="time1" class="post-date" datetime="2017年2月21日星期二凌晨3点21分" title="2017年2月21日星期二凌晨3点21分">'+time+'</time></span>\
        </div>\
        </div>\
        <div class="post-content">\
        <p id="content">'+content+'</p>\
        </div>\
        <div class="post-permalink">\
        <a id="readmore" href="post.html" class="btn btn-default">READ MORE</a>\
        </div>\
        <footer class="post-footer clearfix">\
        <div class = "widget">\
        <div class="content tag-cloud">\
        <a href="/tag/laravel-5/">Laravel 5</a> <a href="/tag/getting-started-with-laravel/">Laravel入门教程</a> <a href="/tag/laravel-5-2/">Laravel 5.2</a>\
        </div>\
        </div>\
        </footer>\
        </article>';

        console.log("iteration:"+i.toString());
        result += str;
        console.log(i+" : "+item.title);
    });
    $("#news").append(result);
    console.log("current_news="+current_news);
}

console.log(".....");

$(document).ready(
    success(J)
);


// for post.html
var find_parent = function() {
    var title = $("#title").text();
    var author = $("#author").text();
    var time = $("#time").text();
    console.log(title);

};
var post_request = function (title,author,time) {
    
};





























