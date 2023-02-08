'''
파일명: urls.py
Description: 로그인/로그 아웃 구현
생성일 : 2/6/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name='common'

urlpatterns = [
    #django.contrib.auth앱의 LoginView 클래스를 활용
    path('login/',auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    #logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.signup,name='signup'),
]