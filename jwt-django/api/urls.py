# -*- coding: utf-8 -*-

"""
Datetime: 2020/04/14
Author: Zhang Yafei
Description: 
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('Login$', views.LoginView.as_view(), name='Login'),
    path("index", views.HomeView.as_view(), name="home"),
    path('upload', views.UploadView.as_view(), name="upload")
]