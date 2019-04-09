from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

class SearchProductView(ListView):
    #queryset = Product.objects.all()  => overriding
    template_name = 'products/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()