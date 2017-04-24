# -----------coding: utf-8-----------
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from firstapp.models import People, Activity
from firstapp.models import Inform
from firstapp.forms import LoginForm
import datetime
from django.contrib.auth.signals import user_logged_in
from django import forms
from django.template import Context, Template
# Create your views here.


def mainpage(request):
    return render(request, 'homepage.html')


def home(request):
    username = 'not login'
    # try and catch to avoid not exists error
    # try and catch to avoid not mutiple value error
    loginer1 = People(name="Acer", major="CS")
    # add: People() -> obj.save()
    # delete: obj.get -> obj.delete()
    # update: obj = People.objects.get(name=""), obj.name = "", obj.save()
    password = ''
    dbuser = People.objects.filter(name=username)
    # order_by, exclude, all,
    if request.method == 'POST':
        # request has two methods and hence two dict, one is POST and another is GET
        loginer = People(name=request.POST.get("username"))
        username = loginer.name
        # <django.forms.widgets.PasswordInput object at 0x03AE1550>
        # password = forms.PasswordInput()
        myLoginForm = LoginForm(request.POST)
        request.session['username'] = username
        if myLoginForm.is_valid():
            username = myLoginForm.clean_data['username']
    # query with condition:People.filter()
    #
    else:
        myLoginForm = LoginForm()
    response = render_to_response('home.html', {'username': username})
    # avoid the situation:    确认重新提交表单
    response.set_cookie('last_connection', datetime.datetime.now())
    response.set_cookie('username', datetime.datetime.now())
    return response
    # return render(request, 'home.html', {'username': username, 'password': password})


def self_info(request):
    # return the info by the cookie's, if not cookies?
    # https://www.tutorialspoint.com/django/django_cookies_handling.htm
    username = request.session['username']
    dbuser = People.objects.filter(name=username)

    if not dbuser:
        return HttpResponse("NOT FOUND USER")
        # raise forms.ValidationError("Not found user")
    else:
        dbuser = dbuser[0]
        return render(request, 'self_info.html', {'user':dbuser})


# Can we not use redirect?
def register(request):
    if request.POST.get('name'):
        postinfo = request.POST
        _name = postinfo.get('name')
        _major = postinfo.get('major')
        _age = postinfo.get('age')
        _grade = postinfo.get('grade')
        newuser = People(name=_name, major=_major, age=_age, grade=_grade)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse("Register Success")
    return render(request, 'register.html')

def watch_activity(request):
    activities = Activity.objects.all()
    #如何解决,如果Activity为空,会有template error, 如果不空的话,没有办法在模板里使用act.name
    #或者要用模板产生一个非正常的act,但是这样显示很奇怪
    if activities:
        return render(request, 'activity.html', {'activities': activities})
    else:
        return render_to_response('activity.html')


def inform(request):
    dic = {}
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
        username = request.COOKIES['username']
        informs = Inform.objects
        if informs:
            informs = informs.filter(accepter = username)
        dic = {'informs': informs}
    return render(request, 'inform.html', dic)


