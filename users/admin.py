from django.contrib import admin
from users.models import User
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ["user_name","email","phone_number"]

admin.site.register(User, AdminUser)    