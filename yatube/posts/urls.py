from django.urls import path

from .views import group_posts, index

app_name = 'posts'

urlpatterns = [
    path('', index, name='main'),  # главная страница
    path('group/<slug:slug>/', group_posts, name='group_list'),
    # страница группы
]
