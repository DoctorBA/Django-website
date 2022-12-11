from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BookView, AuthorsView, AuthorView

# '' - "Домашняя страница"
# 'book/' - Список всех книг
# 'author/' - Список всех авторов
# 'book/<id>' - Детальная информация для отображения книги
# 'author/<id>' - детальная информация для автора
urlpatterns = [
    path('', IndexView.as_view(), name='catalog-index'),
    path('authors/', AuthorsView.as_view(), name='catalog-authors'),
    path('catalog/<str:first_name>-<str:last_name>/', AuthorView.as_view(), name='catalog-author'),
    path('catalog/<int:id>/', BookView.as_view(), name='catalog-book')
]
