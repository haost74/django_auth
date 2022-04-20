from django.http import HttpResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def add_task_to_list(request, id):
    user = get_user_model()
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    html = "<html><body>It is now %s.</body></html>" % request.user.username
    return HttpResponse(html)