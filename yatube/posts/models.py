from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    Модель для постов.
    """
    text = models.TextField('Текст поста', max_length=3000)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='posts_author')
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              verbose_name='Группа', related_name='posts_group',
                              blank=True, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text


class Group(models.Model):
    """
    Модель для групп.
    """
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', max_length=2000)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title
