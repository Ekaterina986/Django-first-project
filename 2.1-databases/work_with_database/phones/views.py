from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = { name: phone.name, price: phone.price }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {phone: phone.slug}
    return render(request, template, context)
