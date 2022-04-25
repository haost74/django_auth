from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import logout
from accounts.models import UserModel

import os.path

from django.template import RequestContext


from django.template.loader import get_template
from django.db import models

#python manage.py makemigrations

#python manage.py migrate --run-syncdb



def add_task_to_list(request, name, id):

    current_user = request.user.username
    isTest = False
    if(request.method == "POST" and 'run_script' in request.POST):
        res = request.POST.get("test[5]")
        #res = request.POST["test[5]"]
        print(res)

    if(current_user == name):
        cn = UserModel.objects.all().filter(iduser=id).count()
        print(cn)
        if(cn == 0):
            u = UserModel(iduser=id, name=name)
            u.save()
        us = UserModel.objects.all().filter(iduser=id)
        return render(request, 'lessons'+str(us[0].lessonsmax)+'.html', {'num': us[0].lessonsmax, 'name': us[0].name, 'id': us[0].iduser})
    else:
        logout(request)
        return render(request, 'home.html')

def next_lesson(request, idlesson, iduser, namep):
    numpage = idlesson + 1
    isexist = os.path.exists('templates/lessons' + str(numpage) + '.html')
    print(isexist)
    if(isexist):
        return render(request, 'lessons' + str(numpage) + '.html',
                  {'num': idlesson, 'name': namep, 'id': iduser})
    else:
        return error_404(request, {}) #render(request, '404.html')

def error_404(request, context):
    context = {}
    return render(request, '404.html', context)



