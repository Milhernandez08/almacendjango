from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from apps.transactions import views

urlpatterns = [
    re_path(r'^transactions/$', views.TransactionsList.as_view() ),
    re_path(r'^transactions/(?P<id>\d+)$', views.TransactionsDetail.as_view() ),
]
