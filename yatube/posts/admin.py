from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Класс подключающий модуль POST в админку
    """
    list_display = ('text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = 'пуста'
    list_editable = ('group',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Класс подключающий модуль GROUP в админку
    """
    list_display = ('title', 'slug', 'description',)
    prepopulated_fields = {'slug': ('title',)}
