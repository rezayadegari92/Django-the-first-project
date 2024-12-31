from django.shortcuts import render
from .models import User
# Create your views here.
def users_show(request):
    users = User.objects
    return render(request, 'users.html',{'users':users})