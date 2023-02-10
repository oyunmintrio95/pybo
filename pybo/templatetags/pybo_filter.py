'''
파일명: pybo_filter.py
Description:
생성일 : 2/3/2023
생성자: oyunm
since 2023.01.09 Copyright (C) by YoungCheon All right reserved.
'''


from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def mark(value):
    '''입력된 문자열을 html로 변환'''
    #nl2br(줄바꿈 문자-><br>, fenced_code(마크다운)
    extensions = ['nl2br','fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter
def sub(value, arg):
    ''' @register.filter:템플릿에서 필터로 사용할수 있게 된다.
        빼기 필터
    '''
    return value - arg
