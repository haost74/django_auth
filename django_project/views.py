from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.db import models

Id = -1



def add_task_to_list(request, name, id):
    global Id
    if (Id == -1):
        Id = id

    current_user = request.user
    print(current_user, name, id)

    address = 'lessons' + str(id) + '.html'
    address = 'lessons' + str(Id) + '.html'

    if(Id == id):
        return render(request, 'lessons1.html')
    else:
        return render(request, 'home.html')
