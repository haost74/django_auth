from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from django.db import models



def add_task_to_list(request, name, id):

    current_user = request.user.username
    print(current_user, name)
    print(current_user == name)

    address = 'lessons' + str(id) + '.html'
    #address = 'lessons' + str(Id) + '.html'
    if(current_user == name):
        return render(request, 'lessons1.html')
    else:
        logout(request)
        return render(request, 'home.html')


