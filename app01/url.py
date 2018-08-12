from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    # url(r'admin',admin.site.urls),
    url(r'^index/',views.index),
    # url(r'^edit/(\w+)/',views.edit)
    # url(r'^edit/(\w+)/(\w+)/',views.edit),
    # url(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/',views.edit)
    url(r'edit/(\w+).html',views.edit),       # 伪静态

]
