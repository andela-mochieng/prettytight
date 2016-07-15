from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)
from .views import *
# Create your views here.
urlpatterns = [
    url(r'^register/$', UserListView.as_view(), name='register'),
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^auth/token/refresh/', refresh_jwt_token),
    url(r'^auth/verify-token/', verify_jwt_token),
]
