'''
파일명: question_views.py
Description:
생성일 : 2/8/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_vote(request, question_id):
    '''질문: 좋아요'''
    logging.info('1.question_vote:{}'.format(question_id))
    # get_object_or_404() 데이타 가져오는 것
    question = get_object_or_404(Question, pk=question_id)

    #본인 글은 추천 하지 못하게
    if request.user == question.author:
        logging.info('2.request.user:{}'.format(request.user))
        logging.info('2.question.author:{}'.format(question.author))
        messages.error(request, '본인이 작성한 글은 추천 할 수 없습니다.')
    else:
        question.voter.add(request.user)

    return redirect('pybo:detail', question_id)


    pass

@login_required(login_url='common:login') #로그인이 되어있지 않으면 login 페이지로 이동
def question_create(request):
    '''질문등록'''

    logging.info('1.request.method:{}'.format(request.method))
    if request.method == 'POST':
        logging.info('2.queston_create post')
        #저장
        form = QuestionForm(request.POST) #request.POST 데이터
        logging.info('3.queston_create post')
        if form.is_valid(): #form(질문등록)이 유효하면 등록
            logging.info('4.form.is_valid():{}'.format(form.is_valid()))
            question = form.save(commit=False) #subject, content만 저장(확정(commit)은 하지 않음.=> 날짜가 없기 때문에)
            question.create_date = timezone.now()
            question.author = request.user #author 속성에 로그인 계정 저장

            logging.info('4.question.author:{}'.format(question.author))
            question.save() #날짜까지 생성해서 저장(Commit)

            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''질문 수정 : login 필수'''
    logging.info('1. question_modify')
    question = get_object_or_404(Question, pk=question_id) #question id로 Question 조회

    #권한 check
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail',question_id = question.id)

    if request.method == 'POST':
        logging.info('2.question_modify post')
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            logging.info('3.form.is_valid():{}'.format(form.is_valid()))
            question = form.save(commit=False) #질문 내용,
            question.modify_date = timezone.now() #수정일시 저장
            question.save() #수정일시까지 생성해서 저장(Commit)
            return redirect("pybo:detail", question_id = question.id)

    else:
        form = QuestionForm(instance = question) #get 수정할 데이터 전달!

    context={'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    logging.info('1.question_delete')
    logging.info('2.question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error('삭제 권한이 잆습니다.')
        return redirect('pybo:detail', question_id = question.id)

    question.delete() #삭제
    return redirect('pybo:index')