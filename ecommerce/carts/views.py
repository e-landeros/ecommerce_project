from django.shortcuts import render, redirect

from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from .models import Cart



def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'carts/home.html', {"cart": cart_obj})

def cart_update(request):
    """
    Add product many to many field into cart
    """
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj) # add product on many to many field. saved on reciever methods
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')

    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
                                                                    user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(
                                                        email=guest_email_obj.email)
    else:
        pass
    if billing_profile is not None:
        #make sure order doesnt exist
        order_qs = Order.objects.filter(cart=cart_obj, active=True)
        if order_qs.exists():
            # if it exists make it inactive
            order_qs.update(active=False)   
        else:
            order_obj = Order.objects.create(
                billing_profile = billing_profile,
                cart=cart_obj)



    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form
    }
    return render(request, "carts/checkout.html", context)