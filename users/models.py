from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$', message="Phone number must be 11 digits .")  
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=11)

    def __str__(self):
        return f"{self.user_name} - {self.email} - {self.phone_number}"