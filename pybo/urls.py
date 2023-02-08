'''
파일명: urls.py
Description: pybo의 모든 URL과 view함수의 메핑 담당!
생성일 : 1/25/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django.urls import path

from . import views #현제 디렉터리의 views 모듈

app_name = 'pybo'

urlpatterns = [
    path('',views.index, name='index'),   #view index로 메핑
    # pybo:detail
    path('<int:question_id>/', views.detail, name='detail'),  # views.py의 detail method


    #answer
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    #pybo:answer_modify
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    #pybo:answer_delete
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),


    #pybo:qustion_create
    path('question/create/',views.question_create, name='question_create'),
    #pybo:qustion_modify
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    #pybo:qustion_delete
    path('question/delete/<int:question_id>',views.question_delete, name='question_delete'),

    #temp menu
    path('boot/menu/', views.boot_menu, name='boot_menu'),
    #bootstrap template
    path('boot/list/',views.boot_list, name='boot_list'),
    path('boot/reg/', views.boot_reg, name='boot_reg'),
    #crawling
    path('crawling/cgv/',views.crawling_cgv, name='crawling_cgv'),

]