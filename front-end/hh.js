var page = 0;
var current_news=0;
var J = [{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"},{"title":"fuck","author":"hh1","time":"2017年2月21日"}];
var get_labels = function(){
    $.get("url...").done
}
var post_request_right = function () {
    if (current_news <= 5) {return false;}
    $.post("{{url_for('hello')}}", page++, success(data));
};  
var post_request_left = function () {
    if (page==0) {return flase;}
    $.post("{{url_for('hello')}}", page--, success(data));
};              
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
        var str = '<article class = "post">\
        <h1 id="title1" class="post-title"><a  href="post.html">'+title+'</a></h1>\
        <div class="post-meta"><span id="author1" class="author">作者：<a href="/author/wangsai/">'+author+'</a></span> &emsp;&bull;<time id="time1" class="post-date" datetime="2017年2月21日星期二凌晨3点21分" title="2017年2月21日星期二凌晨3点21分">'+time+'</time>\
        </div>\
        </div>\
        <div id="content1" class="post-content">\
        <p>'+content+'</p>\
        </div>\
        <div class="post-permalink"><a id="readmore1" href="/post/laravel-5-5-will-be-the-next-lts-release/" class="btn btn-default">read more</a>\
        </div>\
        <footer class="post-footer clearfix">\
        <div class="pull-left tag-list">\
        <i class="fa fa-folder-open-o"></i>\
        <a href="/tag/laravel-5/">Laravel 5</a>, <a href="/tag/getting-started-with-laravel/">Laravel入门教程</a>, <a href="/tag/laravel-5-2/">Laravel 5.2</a>\
        </div>\
        <div class="pull-right share">\
        </div>\
        </footer>\
        </article>'
        console.log("iteration:"+i.toString());
        result += str;
        console.log(i+" : "+item.title);
    });
    $("main").html(result);
    console.log("current_news="+current_news);
}
console.log(".....");

$(document).ready(function(){
    if (page == 0) {
    success(J));
} else {
    post_requst();
    console.log(page);
}
});






