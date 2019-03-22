from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404

from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured-detail.html'

class ProductListView(ListView):
    #queryset = Product.objects.all()  => overriding
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()
    
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'
