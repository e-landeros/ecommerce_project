from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

    context = {
        "title": "hello, Fabian"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "home_page.html")

def contact_page(request):
    return render(request, "home_page.html")