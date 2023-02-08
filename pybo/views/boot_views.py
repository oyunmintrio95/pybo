'''
파일명: boot_views.py
Description:
생성일 : 2/8/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def crawling_cgv(request):
    '''CGV 무비차트'''
    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    response = requests.get(url)

    if 200 == response.status_code:
        html = response.text
        # print('html:{}'.format(html))

        # box-contents
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select('div.box-contents strong.title')
        reserve = soup.select('div.score strong.percent span')
        poster = soup.select('span.thumb-image img')

        title_list=[]
        #예매율
        reserve_list = []
        poster_list = []



        # context={'title':title.getText()}

        for page in range(0, 7, 1):
            posterImg = poster[page]
            # print('posterImg:{}'.format(posterImg))
            imgUrlPath = posterImg.get('src')
            # print('imgUrlPath:{}'.format(imgUrlPath))
            title_list.append(title[page].getText())
            reserve_list.append(reserve[page].getText())
            poster_list.append(imgUrlPath)
            print('title[page]:{},{}'.format(title[page].getText()
                                             , reserve[page].getText()
                                             , imgUrlPath
                                             ))

        context = {'context':zip(title_list,reserve_list,poster_list)}

    else:
        print('접속오류 response.status_code:{}'.format(response.status_code))
    return render(request, 'pybo/crawling_cgv.html', context)

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