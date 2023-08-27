from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects

    # Сортировка
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')

    phonesAll = phones.all()

    context = { "phones": phonesAll }
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    phone = Phone.objects.get(slug = slug)
    context = {"phone": phone}
    return render(request, 'product.html', context)
