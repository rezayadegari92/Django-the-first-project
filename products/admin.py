from django.contrib import admin
from products.models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ["product_name","product_price","category"]
    


admin.site.register(Product, AdminProduct)