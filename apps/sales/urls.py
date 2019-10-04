from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from apps.sales import views

urlpatterns = [
    re_path(r'^sales/$', views.SalesList.as_view() ),
    re_path(r'^sales/(?P<id>\d+)$', views.SalesDetail.as_view() ),
]
