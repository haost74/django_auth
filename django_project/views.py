from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from accounts.models import UserModel

from django.template.loader import get_template
from django.db import models

#python manage.py makemigrations

#python manage.py migrate --run-syncdb


def add_task_to_list(request, name, id):

    current_user = request.user.username
    print(current_user, name)
    print(current_user == name)

    #UserModel.objects.filter(iduser=id).delete()

    address = 'lessons' + str(id) + '.html'
    #address = 'lessons' + str(Id) + '.html'
    if(current_user == name):
        cn = UserModel.objects.all().filter(iduser=id).count()
        print(cn)
        if(cn == 0):
            u = UserModel(iduser=id, name=name)
            u.save()
        us = UserModel.objects.all().filter(iduser=id)
        print(us[0].lessonsmax)
        return render(request, 'lessons'+str(us[0].lessonsmax)+'.html', {'num':us[0].lessonsmax})
    else:
        logout(request)
        return render(request, 'home.html')

def next_lesson(request, idlesson):
    print(request)
    return render(request, 'home.html')


