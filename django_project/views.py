from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from accounts.models import UserModel

import os.path

#from data import checkRes
from django_project.data import checkRes


from django.template import RequestContext


from django.template.loader import get_template
from django.db import models

#python manage.py makemigrations

#python manage.py migrate --run-syncdb



def add_task_to_list(request, name, id):

    current_user = request.user.username
    if(request.method == "POST" and 'run_script' in request.POST):
        us = UserModel.objects.all().filter(iduser=id)
        res = checkRes(request, us[0])
        print(res, 'post', 'add_task_to_list')
        if(res):
            return render(request, 'lessons'+str(us[0].lessonsmax)+'.html',
                          {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 1})
        else:
            return render(request, 'lessons' + str(us[0].lessonsmax) + '.html',
                          {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 2})


    if(current_user == name):
        cn = UserModel.objects.all().filter(iduser=id).count()
        #print(cn)
        if(cn == 0):
            u = UserModel(iduser=id, name=name)
            u.save()
        us = UserModel.objects.all().filter(iduser=id)
        return render(request, 'lessons'+str(us[0].lessonsmax)+'.html', {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 0})
    else:
        logout(request)
        return render(request, 'home.html')

def next_lesson(request, idlesson, iduser, namep, isres):

    current_user = request.user.username

    if (request.method == "POST" and 'run_script' in request.POST):
        us = UserModel.objects.all().filter(iduser=iduser)
        res = checkRes(request, us[0])
        print(res, 'post', 'next_lesson')
        if (res):
            return render(request, 'lessons' + str(us[0].lessonsmax) + '.html',
                          {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 1})
        else:
            return render(request, 'lessons' + str(us[0].lessonsmax) + '.html',
                          {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser, 'isres': 2})

    numpage = idlesson
    if(isres != 5):
        numpage = idlesson + 1
    else:
        numpage = idlesson - 1
    isexist = os.path.exists('templates/lessons' + str(numpage) + '.html')
    print(isres, 'get', 'next_lesson')
    if(isexist):
        us = UserModel.objects.all().filter(iduser=iduser)
        nm = 0
        if(numpage < us[0].lessonsmax):
            nm = 1
        return render(request, 'lessons' + str(numpage) + '.html',
                  {'num': numpage, 'name': namep, 'id': iduser, 'isres': nm})
    else:
        return error_404(request, {}) #render(request, '404.html')

def error_404(request, context):
    context = {}
    return render(request, '404.html', context)



