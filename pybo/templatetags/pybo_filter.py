from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value-arg

# 위처럼 sub 함수에 @register.filter 라는 어노테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다. sub 함수는 기존 값(value)에서 입력으로 받은 값(arg)을 빼서 리턴하는 필터이다.

