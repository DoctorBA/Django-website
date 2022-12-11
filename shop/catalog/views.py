from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book
from .models import Author


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request):
        books = Book.objects.all()
        numb = books.count()
        authors = Author.objects.all().count()
        
        return render(request, self.template_name, {'books': books, 'numb': numb, 'authors': authors})


class AuthorsView(TemplateView):
    template_name = 'catalog/authors.html'
    
    def get(self, request):
        authors = Author.objects.all()
        return render(request, self.template_name, {'authors': authors})

class BookView(TemplateView):
    template_name = 'catalog/book.html'
    
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, self.template_name, {'book': book})
    

class AuthorView(TemplateView):
    template_name = 'catalog/index.html'
    
    def get(self, request, first_name, last_name):
        author = Author.objects.get(first_name=first_name, last_name=last_name)
        books = Book.objects.filter(author=author)
        return render(request, self.template_name, {'author':author, 'books': books})
         
        