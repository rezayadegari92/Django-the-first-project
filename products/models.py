from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('OPTION1','Furniture'),
        ('OPTION2','Electronic')
        ]
    product_name = models.CharField(max_length=30)
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=20,choises=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.product_name} - {self.product_price} - {self.category}"