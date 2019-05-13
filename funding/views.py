from django.shortcuts import render
from .models import User
# Create your views here.

def user (request, id):
    userSet = User.objects.filter(id = id)
    for oneUser in userSet:
        user = oneUser
    return render(request, 'users/show.html', {'user':user})