from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

class SearchProductView(ListView):
    #queryset = Product.objects.all()  => overriding
    template_name = 'products/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        print(method_dict)
        query = request.GET.get('q') # equivilent to method_dict['q'] but get() method doesnt have error on none
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()

        '''
        __icontains = field contains this
        __iexact = field is exactly this 
        '''