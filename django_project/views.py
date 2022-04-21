from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render


def add_task_to_list(request, id):
    return render(request, 'lessons1.html')