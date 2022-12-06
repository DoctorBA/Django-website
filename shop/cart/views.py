from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cart


class Cart(TemplateView):
    template_name = 'Cart/Cart.html'
    
    def get(self, request):
        return render(request, self.template_name)


