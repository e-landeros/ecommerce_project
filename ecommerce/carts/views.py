from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', {})

def cart_update(request):
    """
    Add product many to many field into cart
    """
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    cart_obj.products.add(product_obj) # add product on many to many field. saved on reciever methods

    return redirect("cart:home")
