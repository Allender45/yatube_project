from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main'),  # главная страница
    path('group/<slug:slug>/', group_posts, name='group_posts'),  # страница групп
]
