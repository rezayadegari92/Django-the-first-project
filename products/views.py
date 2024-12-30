from django.shortcuts import render
from .models import Product

# Create your views here.
def products_show(request):
    products = Product.objects.filter(available=True)
    return render(request, 'store.html',{'products':products})