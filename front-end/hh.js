// for copy.html
var $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
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
    $.post(SCRIPT_ROOT+'/_return_new_by_year', page++, success(data));
};  
var copy_left = function () {
    if (page==0) {return false;}
    $.post("{{url_for('/')}}", page--, success(data));
}; 

$(".previous").click(copy_left()); 
$(".next").click(copy_right());

var success = function(data) {
    console.log("#####success#####");
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
        var label = item.label;
        var label_html = function (labels) {
            var result_labels = ''
            $.each(labels,function(i,subitem) {
                result_labels += '<a id = "label" href="copylaravel.html">'+subitem+'</a>';
            });
            return result_labels;
        };

        var label_html = label_html(label); // 这里是数组，返回html文本分

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
        <div class="content tag-cloud">'+label_html+'</div>\
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
    console.log("#### hh.js ###");
    $.post(SCRIPT_ROOT+'/_return_news_by_year',[2015,1],function(data){
        success(data);
    });
);

// for copy.html to post.html
var post_request = function () {
    var title = $("#title").text();
    var author = $("#author").text();
    var time = $("#time").text();
    console.log("to post.html"+title);
    $.post("{{url_for('post')",{"title":title,"author":author,"time",time},function (json) {
        set_up_post(title,author,time);
    });
};
$.("#title").click(post_request());
$.("#readmore").click(post_request());

// for copy.html
var set_up_post = function (title, author, time) {
    $ ("#post-title").text(title);
    $ ("#post-author").text(author);
    $ ("#post-time").text(time);
    // $ ("#post-content").text(time);
};

// for copy.html to person.html

var person_request = function () {
    var title = $("#title").text();
    var author = $("#author").text();
    var time = $("#time").text();
    console.log("to person.html"+author);
    $.post("{{url_for('person')",{"title":title,"author":author,"time",time},function (json) {
        set_up_person(title,author,time);
    });
}

var set_up_person = function (title, author, time) {
    $ ("#post-title").text(title);
    $ ("#person-name").text("作者："+name);
    $ ("#post-time").text(time);
    // $ ("#post-content").text(time);
};

var search_label = function () {

};
























