from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from homework.my_f import hw_sum_even


# Create your views here.
def hw_even (request: WSGIRequest):
    request_data_dict = dict(request.GET.items())
    a = int(request_data_dict['start'])
    b = int(request_data_dict['end'])
    return render(
        request,
        'sum_even_hw.html',
        {'result': hw_sum_even(a, b)}
    )

