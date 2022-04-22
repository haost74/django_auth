# django_project/urls.py
from django import forms
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('view/<str:name>/<int:id>/', views.add_task_to_list, name='add_task'),
    path('view/<int:idlesson>/', views.next_lesson, name='new_lessons'),
]


