from re import sub
from django import template


register = template.Library()


@register.filter(name='censor')
def censor(value, arg):
    text_no_censor = str(value)
    words = ['блин', 'гад', 'лох']

    for word in words:
        text_no_censor = sub(word, str(arg), text_no_censor)

    return text_no_censor

