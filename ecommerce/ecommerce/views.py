from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm 

def home_page(request):

    context = {
        "title": "Home Page",
        "content": "hello, Fabian",
    }
    # if request.user.is_authenticated():
    #     context["premium_content"] = "YEAH" 
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "home_page.html")

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
        'title': 'contact',
        'content': 'welcome to the contact page',
        'brand': 'new Brand Name'
    }

    if  contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, "contact/view.html", context)

