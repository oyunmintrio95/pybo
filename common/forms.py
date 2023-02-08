'''
파일명: forms.py
Description: 회원가입 form
생성일 : 2/6/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ('username','password1','password2','email')

