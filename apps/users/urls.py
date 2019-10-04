from django.urls import path, re_path
from django.conf.urls import include
# from rest_framework import routers, serilizers, viewsets
from apps.users.views import CustomAuthToken, UsersList, UsersDetail
from apps.users import views

urlpatterns = [
    re_path(r'^login', CustomAuthToken.as_view()),
    re_path(r'^users/$', UsersList.as_view() ),
    re_path(r'^users/(?P<id>\d+)$', UsersDetail.as_view() ),
]
