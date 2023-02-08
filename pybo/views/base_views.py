'''
파일명: base_views.py
Description:
생성일 : 2/8/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
import logging

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def detail(request, question_id):
    '''question 상세'''
    logging.info('1. question_id:{}'.format(question_id))
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id)
    logging.info('2. question:{}'.format(question))
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context)

def index(request):
    '''question 목록'''
    # Question.objects.order_by('create_date') #=>ASC
    logging.info('index 레벨로 출력')
    # print('index 레벨로 출력')
    #list order create_date desc

    #입력인자: http://127.0.0.1:8000/pybo/1
    page = request.GET.get('page','1')
    logging.info('page:{}'.format(page))

    question_list = Question.objects.order_by('-create_date') # order_by('-필드')=>DESC
    #paging

    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)

    # paginator.count: 전체 게시물 개수
    # paginator.per_oage:페이지당 보여줄 게시물 개수
    # paginator.per_range: 페이지 범위
    # number: 현재 페이지 번호
    # previous_page_number: 이전 페이지 번호
    # next_page_number: 다음 페이지 번호
    # has_previous: 이전 페이지 유무
    # has_naext: 다음 페이지 유무
    # start_index : 현재 페이지 시작 인덱스(1부터 시작)
    # end_index: 현재 페이지 끝 인덱스


    # question_list = Question.objects.filter(id=99)
    context = {'question_list':page_obj}
    logging.info('question_list:{}'.format(page_obj))

    return render(request,'pybo/question_list.html',context)