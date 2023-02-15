import logging

from django.contrib import messages
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from board.forms import BoardForm
from pybo.models import Board

@login_required(login_url='common:login')
def board_delete(request, board_id):
    '''게시물 삭제'''
    logging.info('1.board_delete')
    logging.info('2.board_id:{}'.format(board_id))
    board = get_object_or_404(Board, pk=board_id)

    if request.user != board.author:
        messages.error('삭제 권한이 없습니다.')
        return redirect('board:board_detail', board_id=board.id)

    board.delete()
    return redirect('board:board_list')

@login_required(login_url='common:login')
def board_modify(request, board_id):
    '''게시물 수정'''
    logging.info('1.board_modify')
    board = get_object_or_404(Board,pk=board_id)

    if request.user != board.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('board:board_detail', board_id = board.id)
    if request.method == 'POST':
        logging.info('2.question_modify post')
        form = BoardForm(request.POST, instance=board)

        if form.is_valid():
            logging.info('3.form.is_valid:{}'.format(form.is_valid()))
            board = form.save(commit=False)
            board.modify_date = timezone.now()
            board.save()
            return redirect("board:board_detail",board_id=board.id)
    else:
        form = BoardForm(instance=board)
    context = {'form':form}
    return render(request, 'board/board_form.html', context)

def board_detail(request, board_id):
    '''게시물 상세'''
    logging.info('1.board_id:{}'.format(board_id))
    board = get_object_or_404(Board, pk=board_id)

    logging.info('2.board:{}'.format(board))
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)

@login_required(login_url='common:login')
def board_create(request):
    '''게시물 등록'''
    logging.info('1.request.method:{}'.format(request.method))
    if request.method == 'POST':
        logging.info('2.board_create post')
        form = BoardForm(request.POST)
        logging.info('3.board_create post')
        if form.is_valid():
            logging.info('4.form.is_valid():{}'.format(form.is_valid()))
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.author = request.user

            logging.info('4.board.author:{}'.format(board.author))

            board.save()
            return redirect("board:board_list")
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request, 'board/board_form.html', context)



# Create your views here.
def board_list(request):
    '''board 목록'''
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    div = request.GET.get('div', '')
    size = request.GET.get('size', '10')

    logging.info('page:{}'.format(page))
    logging.info('kw:{}'.format(kw))
    logging.info('div:{}'.format(div))
    logging.info('size:{}'.format(size))

    board_list = Board.objects.order_by('-create_date')

    if '10' == div:
        logging.info('if 10')
        board_list = board_list.filter(subject_contains=kw)
    elif '20' == div:
        logging.info('elif 20')
        board_list = board_list.filter(content_contains=kw)
    elif '30' == div:
        logging.info('elif 30')
        question_list = board_list.filter(author__username__contains=kw)

    paginator = Paginator(board_list, size)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'kw': kw, 'page':page, 'div': div, 'size':size}
    logging.info('board_list:{}'.format(page_obj))

    return render(request, 'board/list.html', context)

