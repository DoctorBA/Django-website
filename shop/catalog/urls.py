from django.contrib import admin
from django.urls import path, include
from .views import IndexView

# '' - "Домашняя страница"
# 'book/' - Список всех книг
# 'author/' - Список всех авторов
# 'book/<id>' - Детальная информация для отображения книги
# 'author/<id>' - детальная информация для автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index')
]
