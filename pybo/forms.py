'''
파일명: forms.py
Description: html form 관리
생성일 : 2/1/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django import forms
from pybo.models import Question, Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        
        fields = ['content']
        
        labels = {
            'content': '답변 내용'
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 question model

        fields = ['subject','content'] #QuestionForm에서 사용할 question model의 속성들

        labels = {
            'subject' : '제목',
            'content' : '내용',
        }

