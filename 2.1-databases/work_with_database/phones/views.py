from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()  # Получаем все телефоны
    sort_option = request.GET.get('sort')

    if sort_option == 'name':
        phones = phones.order_by('name')
    elif sort_option == 'min_price':
        phones = phones.order_by('price')
    elif sort_option == 'max_price':
        phones = phones.order_by('-price')

    template = 'catalog.html'
    context = {'phones': phones}  # Передаем телефоны в контекст
    return render(request, template, context)


def show_product(request, slug):
    try:
        phone = Phone.objects.get(slug=slug)  # Пытаемся получить телефон по слагу
    except Phone.DoesNotExist:
        return HttpResponse(status=404)  # Если телефон не найден, возвращаем 404

    template = 'product.html'
    context = {'phone': phone}  # Передаем телефон в контекст
    return render(request, template, context)