from django.shortcuts import render
from .models import Product

# Create your views here.
def products_show(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products.html',{'products':products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'pro_detaile.html',{'product':product})    