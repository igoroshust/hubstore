from django import template
from goods.models import Categories

# Регистрация шаблона
register = template.Library()

@register.simple_tag()  # Позволяет вызвать функцию в шаблоне
def tag_categories():
    return Categories.objects.all()