"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    # url(r'^index/(\d+)',views.index,name='n1'), # 根据名称反生成url
    # url(r'^index/(?P<a1>\d+)/',views.index,name='n1'),
    url(r'^login/',views.login,name='l1'),
    url(r'index/',views.index,name='n1'),
    # url(r'edit/(\w+)/',views.edit,name='n2'),
    url(r'edit/(\w+)/(\w+)',views.edit,name='n2')

    # url(r'',views.index)
    # url(r'app01/', include('app01.url')),
    # url(r'app02/',include('app02.url'))

]
