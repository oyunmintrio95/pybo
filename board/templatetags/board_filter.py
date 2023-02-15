import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    '''입력된 문자열을 html로 변환'''
    extensions = ['nl2br','fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extensions))
