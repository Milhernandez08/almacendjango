from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from apps.products import views

urlpatterns = [
    re_path(r'^products/$', views.ProductsList.as_view() ),
    re_path(r'^products/(?P<id>\d+)$', views.ProductsDetail.as_view() ),
]
