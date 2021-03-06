"""myechartsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as lv
from djoncharts import views as djv
from django.views.generic.base import RedirectView
import django

urlpatterns = [
    url(r'^admin', admin.site.urls),#zhexian/$
    url(r'zhexian',djv.zhexian, name='zhexian'),
    url(r'^index', lv.index1),
    url(r'^run', lv.run),
    url(r'^chr', lv.chr),
    url(r'^xr', lv.xr),
    url(r'^show',djv.show),
    url(r'^adduser',djv.adduser),
    url(r'viradd',djv.virus),

    # url(r'^accounts/', users.urls),

    url(r'water',djv.water),#RedirectView.as_view(url=r'static/images/favicon.ico')
    # url(r'^accounts/login', 'django.contrib.auth.views.login'),
    #     # #^water
]
