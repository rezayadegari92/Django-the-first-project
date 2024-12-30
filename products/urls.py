from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.products_show, name='home')
]