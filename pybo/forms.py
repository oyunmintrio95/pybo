'''
파일명: forms.py
Description: html form 관리
생성일 : 2/1/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 question model

        fields = ['subject','content'] #QuestionForm에서 사용할 question model의 속성들
        widgets = { #속성 추가: class rows추가
            #class ="form-control"
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control','rows':10})
        }
        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

