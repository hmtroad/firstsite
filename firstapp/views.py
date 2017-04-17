from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render_to_response
from firstapp.models import People, Article
from firstapp.forms import LoginForm
from django import forms
from django.template import Context, Template
# Create your views here.


def first_try(request):
    person = People(name='Spock', job='officer')
    html_string = '''
    <html>
        <head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.4/semantics.css">
        </head>
        <body>
        <h1 class="ui center aligned icon header">
            <i class="hand spock icon "></i>
            Hello {{person.name}}
        </h1>
        </body>
    </html>'''
    t = Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)
    return HttpResponse(web_page)

def mainpage(request):
    return render(request, 'homepage.html')

def index(request):
    context = {}
    article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'homepage.html', context)
    return index_page

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
    return render_to_response('home.html', {'username': username})
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

#Can we not use redirect?
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