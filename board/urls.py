'''
파일명: urls.py
Description:
생성일 : 2/15/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django.urls import path

from . import views
from .views import board_list

app_name = 'board'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('board_create/', views.board_create, name='board_create'),
    path('board_detail/<int:board_id>/', views.board_detail, name='board_detail'),
    path('board_modify/<int:board_id>/', views.board_modify, name='board_modify'),
    path('board_delete/<int:board_id>/', views.board_delete, name='board_delete'),
]