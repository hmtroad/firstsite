"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import mainpage, home
from firstapp.views import self_info, register
from firstapp.views import watch_activity, inform

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage, name="mainpage"),
    url(r'^home$', home, name="home"),
    url(r'^home', mainpage, name="mainpage"),
    # need cookie?
    url(r'^self_info$', self_info, name="self_info"),
    url(r'^register$', register, name="register"),
    url(r'^activity$', watch_activity, name="watch_activity"),
    url(r'^inform$', inform, name="inform"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
