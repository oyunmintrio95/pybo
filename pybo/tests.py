import datetime
import unittest

from django.test import TestCase

import unittest
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Create your tests here.
class Crawling(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def teardown(self):
        print('tearDown')

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
                price = soup.select_onew('#chart_area div.rate_info div.today span.blind')
                print('price:{}'.format(price.getText()))

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

                # print('평점, 감상평:{},{}')

    @unittest.skip
    def test_slemdunk(self):
        '''naver영화'''
        url= ''
        for i in range (1,4,1):
            self.call_slemdunk(url +str(i))
    @unittest.skip
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
