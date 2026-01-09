from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Представление (контроллер) для главной страницы"""
    context = {"title": "Home - Главная", "content": "Магазин мебели HOME"}

    return render(request, "main/index.html", context)


def about(request):
    """О нас"""
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том, почему этот магазин такой классный, и какой хороший товар",
    }

    return render(request, "main/about.html", context)