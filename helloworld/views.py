from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse

# Create your views here.

def hello_time(request):
    now = datetime.datetime.now()
    html = "<html><h2>Hello!</h2><body>It is now %s.</body>" % now
    return HttpResponse(html)

def hello_year(request, year):
    html = "<html><h2>Hello!</h2><body>It is %s.</body></html>" % year
    return HttpResponse(html)

def json_data(request, data):
    response_data = {
        "hello": "Hello:",
        "data": data,
        "method": request.method,
        "url": request.path
    }
    return JsonResponse(response_data)