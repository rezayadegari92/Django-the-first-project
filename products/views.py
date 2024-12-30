from django.shortcuts import render

# Create your views here.
def products_show(request):
    return render(request, 'store.html')