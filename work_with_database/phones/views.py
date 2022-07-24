from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        context = {
            'phones': Phone.objects.all().order_by('name')
        }
    elif sorting == 'min_price':
        context = {
            'phones': Phone.objects.all().order_by('price')
        }
    elif sorting == 'max_price':
        context = {
            'phones': Phone.objects.all().order_by('-price')
        }
    else:
        context = {
            'phones': Phone.objects.all()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug).first()
    }
    return render(request, template, context=context)
