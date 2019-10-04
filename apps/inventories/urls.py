from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets

from apps.inventories import views

urlpatterns = [
    re_path(r'^inventories/$', views.InventoriesList.as_view() ),
    re_path(r'^inventories/(?P<id>\d+)$', views.InventoriesDetail.as_view() ),
]
 