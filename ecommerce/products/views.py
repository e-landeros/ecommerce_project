from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'