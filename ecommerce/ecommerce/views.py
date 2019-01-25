from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):

    context = {
        "title": "hello, Fabian"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    return render(request, "home_page.html")

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form": contact_form,
        'title': 'contact',
        'content': 'welcome to the contact page'
    }

    if  contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)