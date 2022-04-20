from django.http import HttpResponse
import datetime

def add_task_to_list(request, id):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)