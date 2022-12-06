from django.urls import path, include
from .views import Cart


urlpatterns = [
    path('', Cart.as_view(), name='catalog-index')
]