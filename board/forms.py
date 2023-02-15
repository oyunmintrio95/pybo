'''
파일명: forms.py
Description:
생성일 : 2/15/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''
from django import forms

from pybo.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board

        fields = ['subject','content']

        labels = {
            'subject' : '제목',
            'content' : '내용',
        }