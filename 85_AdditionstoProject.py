#Day 85 - Some additions to Python and HTML documents

#to views.py:

def test_view(*args, **kwargs):
    return HttpResponse("<h1>This is a test page.</h1>")
    

to urls.py:

path('test/', views.test_view),

to base.html:

#<div id="loginbox">
        #Hello, {{ request.user }}.
#</div>

#to styles.css:

##loginbox {
    #font-size: 20px;
    #float: right;
    #width: auto;
    #height: auto;
    #border: 4px solid #5C8DBB;




}
