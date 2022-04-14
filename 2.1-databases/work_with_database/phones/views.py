from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_field = request.GET.get('sort', None)
    if sort_field:
        phones = Phone.objects.order_by(sort_field)
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'slug': slug,
        'phone': phone
    }
    return render(request, template, context)
