from django.db import models
from catalog.models import Book


class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    price = models.FloatField()
        
    def __str__(self):
        return self.book
