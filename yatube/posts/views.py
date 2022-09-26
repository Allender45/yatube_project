from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


def index(request: object):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug) -> HttpResponse:
    """
    Вью функция страницы конкретной группы
    :param : slug, request
    :return : HttpResponse
    """

    group = get_object_or_404(Group, slug=slug)  # проверка наличия группы
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]  # выборка постов

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
