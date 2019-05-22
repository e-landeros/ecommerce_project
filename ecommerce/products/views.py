from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from carts.models import Cart
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured-detail.html'

class ProductFeaturedSlugDetailView(DetailView):
    queryset = Product.objects.all()
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
        

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("uhmm...")
        return instance

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'
