from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.products_show, name='products'),
    path('products/<int:id>', views.product_detail, name='product_view')
]