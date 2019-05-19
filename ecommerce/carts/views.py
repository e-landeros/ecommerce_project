from django.shortcuts import render

from .models import Cart

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None: #and isinstance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print('Cart ID exists')
    #print(request.session)
    #print(dir(request.session))
    #key = request.session.session_key
    #print(key)
    return render(request, 'carts/home.html', {})
