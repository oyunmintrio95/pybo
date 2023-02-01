from django.utils import timezone

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Question,Answer
from .forms import QuestionForm, AnswerForm
import logging

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
            question.save() #날짜까지 생성해서 저장(Commit)
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

#bootstrap list
def boot_menu(request):
    '''개발에 사용되는 임시 메뉴'''
    return render(request, 'pybo/menu.html')
def boot_reg(request):
    '''bootstrap register template'''
    return render(request, 'pybo/reg.html')

def boot_list(request):
    '''bootstrap template'''
    return render(request,'pybo/list.html')

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
            answer.save() #최종 저장
            return redirect('pybo:detail', question_id=question_id)
    else:
        return HttpResponseNotAllowed('POST만 가능 합니다.')

    #form validation
    context = {'question':question, 'form':form}
    return render(request,'pybo/question_detail.html', context)
    # Question과 Answer 처럼 서로 연결되어 있는 경우 연결 모델명 _set 연결데이터를 조회 할 수 있다.
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail',question_id=question_id)


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
    question_list = Question.objects.order_by('-create_date') # order_by('-필드')=>DESC
    # question_list = Question.objects.filter(id=99)
    context = {'question_list':question_list}
    logging.info('question_list:{}'.format(question_list))

    return render(request,'pybo/question_list.html',context)



