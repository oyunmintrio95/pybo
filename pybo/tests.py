import datetime
import unittest

from django.test import TestCase

import unittest
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyperclip    #클립보드를 쉽게 활용할 수 있게 해주는 모듈
from selenium.webdriver.common.keys import Keys #Ctrl+c, Ctrl+v

from pybo.models import Question
from django.utils import timezone

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# from user.models import Users

# q = Question(subject='장고 페이지네이션 하는 중.[%3d]' %i, content='페이지네이션 되는 거 맞지? 왜 장고 쉘에서 하는거야? 다 도스창 같이 생겨서 되게 헷갈림ㅠㅠㅠ 저 퍼센트 아이는 뭘까..', create_date=timezone.now())
# q.save()

# Create your tests here.
class Crawling(unittest.TestCase):
    def setUp(self):
        #webdriver Firefox 객체 생성
        self.browser = webdriver.Firefox(executable_path='C:/BIG_AI0102/01_PYTHON_BASIC/app/geckodriver.exe')
        print('setUp')

    def teardown(self):
        logging.info('tearDown')
        #self.browser.quit() #webdriver 종료

    def test_clipboard_naver(self):
        '''clipboard를 통한 naver login'''
        self.browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        user_id = 'cjsgkdud9500'
        user_pw ='Epdlxk5104!'

        #id
        id_textinput = self.browser.find_element(By.ID, 'id')
        id_textinput.click()
        #클립보드 copy
        pyperclip.copy(user_id)
        id_textinput.send_keys(Keys.CONTROL,'v')
        time.sleep(1)


        #password
        pw_textinput = self.browser.find_element(By.ID,'pw')
        pw_textinput.click()
        pyperclip.copy(user_pw)
        pw_textinput.send_keys(Keys.CONTROL,'v')
        time.sleep(1)

        #로그인 버튼
        btn_login = self.browser.find_element(By.ID,'log.login')
        btn_login.click()
        pass

    @unittest.skip('test_naver')
    def test_naver(self):
        self.browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

        #아이디
        login_user = self.browser.find_element(By.ID,'id')
        login_user.send_keys("cjsgkdud9500")
        #비번
        login_pw = self.browser.find_element(By.ID,'pw')
        login_pw.send_keys('Epdlxk5104!')

        btn_login = self.browser.find_element(By.ID, 'log.login')
        btn_login.click()
        pass


    @unittest.skip('text_selenum')
    def test_selenium(self):
        #FireFox 웹 드라이버 객체에게 Get을 통하여 네이버의 http요청을 하게 함.
        self.browser.get('http://127.0.0.1:8000/pybo/1/')
        print('self.browser.title:{}'.format(self.browser.title))
        self.assertIn('Pybo',self.browser.title)

        content_textarea = self.browser.find_element(By.ID, 'content')
        content_textarea.send_keys('오늘은 아주 즐거운 금요일2!')
        content_btn = self.browser.find_element(By.ID, 'submit-btn')
        content_btn.submit()
        # content_btn.click()
        pass

    @unittest.skip('text_zip')
    def test_zip(self):
        '''여러개의 list를 묶어서 하나의 iterable 객체로 다룰 수 있게 한다.'''
        integers = [1,2,3]
        letters = ['a','b','c']
        floats = [4.0, 8.0, 10.0]
        zipped = zip(integers,letters,floats)

        list_data = list(zipped)
        print('list_data:{}'.format(list_data))
        pass

    @unittest.skip('test_naver_stock')
    def test_naver_stock(self):
        '''주식 크롤링'''
        codes = {'삼성전자':'005930', '현대차':'005380'}
        for code in codes.keys():
            url = 'https://finance.naver.com/item/main.naver?code='
            url = url + str(codes[code])
            response = requests.get(url)

            if 200 == response.status_code:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # price = soup.select_one('p.no_today span.blind')
                price = soup.select_one('#chart_area div.rate_info div.today span.blind')
                print('price:{}'.format(price.getText()))
                today = price.select_one('.blind')
                print('today:{},{},{}'.format(code,codes[code],price.getText()))

            else:
                print('접속오류 response.status_code:{}'.format(response.status_code))

    @unittest.skip
    def call_slemdunk(self, url):
        response=requests.get(url)
        if 200 == response.status_code:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            score = soup.select('div.list_netizen_score em')
            review = soup.select('table tbody tr td.title')

            for i in range(0, len(score)):
                review_text = review.getText()

                if len(review_text) >2: #평점만 넣고 감상평 없는 경우 처리
                    tmp_text = review_text[5]
                else:
                    tmp_text = review_text[0]

                print('평점, 감상평:{},{}'.format(score[i].getText(), tmp_text))
        else:
            print('접속오류 response.statuse_code:{}'.format(response.status_code))
    @unittest.skip
    def test_slemdunk(self):
        '''naver영화'''
        url= 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page='
        for i in range (1,4,1):
            self.call_slemdunk(url +str(i))
    @unittest.skip('slemdunk')
    def test_cgv(self):
        '''http://www.cgv.co.kr/movies/?lt=1&ft=0'''
        url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
        response = requests.get(url)

        if 200 == response.status_code:
            html = response.text
            # print('html:{}'.format(html))

            #box-contents
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.select('div.box-contents strong.title')
            reserve = soup.select('div.score strong.percent span')
            poster = soup.select('span.thumb-image img')

            for page in range(0, 7, 1):
                posterImg = poster[page]
                # print('posterImg:{}'.format(posterImg))
                imgUrlPath = posterImg.get('src')
                # print('imgUrlPath:{}'.format(imgUrlPath))
                print('title[page]:{},{}'.format(title[page].getText()
                                                 , reserve[page].getText()
                                                 ,imgUrlPath
                                                 ))

        else:
            print('접속오류 response.status_code:{}'.format(response.status_code))



    @unittest.skip("테스트 연습")
    def test_weather(self):
        '''날씨'''
        # https://weather.naver.com/today/09545101
        now = datetime.datetime.now()
        #yyyymmdd hh:mm
        newDate = now.strftime('%Y-%m-%d %H:%M:%S')
        print('='*35)
        print(newDate)
        print('='*35)

        #-------------------------------------------------------------
        naverWetherUrl = 'https://weather.naver.com/today/09545101'
        html = urlopen(naverWetherUrl)
        # print('html:{}'.format(html))
        bsObject = BeautifulSoup(html, 'html.parser')
        tmpes = bsObject.find('strong','current')
        print('서울 마포구 서교동:{}'.format(tmpes.text))



        print('test_weather')
