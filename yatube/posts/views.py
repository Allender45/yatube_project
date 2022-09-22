from django.shortcuts import render
from django.http import HttpResponse


def index(request: object) -> HttpResponse:
    """
    Вью функция главной страницы
    :param : request
    :return : HttpResponse
    """
    return HttpResponse('Главная страница')


def group_posts(request, slug) -> HttpResponse:
    """
    Вью функция страницы конкретной группы
    :param : slug, request
    :return : HttpResponse
    """
    return HttpResponse(f'Посты группы {slug}')
