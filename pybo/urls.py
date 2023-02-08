'''
파일명: urls.py
Description: pybo의 모든 URL과 view함수의 메핑 담당!
생성일 : 1/25/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django.urls import path
from .views import base_views, question_views, answer_views, boot_views

app_name = 'pybo'

urlpatterns = [
    #base_view
    path('',base_views.index, name='index'),   #view index로 메핑
    # pybo:detail
    path('<int:question_id>/', base_views.detail, name='detail'),  # views.py의 detail method


    #answer
    path('answer/create/<int:question_id>/',answer_views.answer_create,name='answer_create'),
    #pybo:answer_modify
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    #pybo:answer_delete
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),


    #question
    #pybo:qustion_create
    path('question/create/',question_views.question_create, name='question_create'),
    #pybo:qustion_modify
    path('question/modify/<int:question_id>', question_views.question_modify, name='question_modify'),
    #pybo:qustion_delete
    path('question/delete/<int:question_id>',question_views.question_delete, name='question_delete'),

    #boot
    #temp menu
    path('boot/menu/', boot_views.boot_menu, name='boot_menu'),
    #bootstrap template
    path('boot/list/',boot_views.boot_list, name='boot_list'),
    path('boot/reg/', boot_views.boot_reg, name='boot_reg'),
    #crawling
    path('crawling/cgv/',views.crawling_cgv, name='crawling_cgv'),

]