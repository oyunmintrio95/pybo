'''
파일명: answer_views.py
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

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    logging.info('1.answer_delete:{}'.format(answer_id))
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error('삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id = answer.question.id)
    logging.info('2.right before deleteing')
    answer.delete()
    logging.info('3.deleted')

    return redirect('pybo:detail', question_id=answer.question.id)
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    logging.info('1.answer_modify:{}'.format(answer_id))
    #1.answer id에 해당되는 데이터 조회
    #2.수정 권한 체크: 권한이 없는 경우 메시지 전달
    #3. POST: 수정
    #4. GET : 수정 Form 전달

    #1.
    answer=get_object_or_404(Answer, pk=answer_id)
    #2.
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail',question_id=answer.question.id)
    #3.
    if request.method == "POST": #수정
        form = AnswerForm(request.POST, instance=answer)
        logging.info('2.answer_modify POST answer:{}'.format(answer))

        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            logging.info('3.answer_modify POST form.is_valid:{}'.format(answer))
            answer = form.save()
            #수정화면
            return redirect('pybo:detail', question_id=answer.question.id)
    else:                       #수정 form template
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form':form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    '''답변 등록'''

    logging.info('answer_crete question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) #content만 저장하고 확정은 하지 않음.
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user  # author 속성에 로그인 계정 저장

            logging.info('3.answer.author:{}'.format(answer.author))
            answer.save() #최종 저장
            return redirect('pybo:detail', question_id=question_id)
    else:
        logging.info('1.else:{}')
        form = AnswerForm()

    #form validation
    context = {'question':question, 'form':form}
    return render(request,'pybo/question_detail.html', context)
    # Question과 Answer 처럼 서로 연결되어 있는 경우 연결 모델명 _set 연결데이터를 조회 할 수 있다.
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail',question_id=question_id)
