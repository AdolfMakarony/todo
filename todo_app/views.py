from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: WSGIRequest):
    return render(
        request,
        'index.html',
        {'name' : 'test'})


def huindex(request):
    return HttpResponse('<h1>Bye bye world!</h1>')
