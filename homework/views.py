from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from homework.service.my_f import hw_sum_even


# Create your views here.
def hw_even(request: WSGIRequest):
    request_data_dict = dict(request.GET.items())
    a = int(request_data_dict['start'])
    b = int(request_data_dict['end'])
    return render(
        request,
        'sum_even_hw.html',
        {'result': hw_sum_even(a, b)}
    )


def hw_sentence_case(request: WSGIRequest):
    if request.method == 'GET':
        return render(
            request,
            'text_change.html',
            {'text': '-'}
        )
    else:
        request_data = str(dict(request.POST.items())['text']).capitalize()
        return render(
            request,
            'text_change.html',
            {'text': request_data}
        )
def hw_lower_case(request: WSGIRequest):
    if request.method == 'GET':
        return render(
            request,
            'text_change.html',
            {'text': '-'}
        )
    else:
        request_data = str(dict(request.POST.items())['text']).lower()
        return render(
            request,
            'text_change.html',
            {'text': request_data}
        )
def hw_upper_case(request: WSGIRequest):
    if request.method == 'GET':
        return render(
            request,
            'text_change.html',
            {'text': '-'}
        )
    else:
        request_data = str(dict(request.POST.items())['text']).upper()
        return render(
            request,
            'text_change.html',
            {'text': request_data}
        )
def hw_cap_word_case(request: WSGIRequest):
    if request.method == 'GET':
        return render(
            request,
            'text_change.html',
            {'text': '-'}
        )
    else:
        request_data = str(dict(request.POST.items())['text']).title()
        return render(
            request,
            'text_change.html',
            {'text': request_data}
        )
def hw_toggle_case(request: WSGIRequest):
    if request.method == 'GET':
        return render(
            request,
            'text_change.html',
            {'text': '-'}
        )
    else:
        request_data = str(dict(request.POST.items())['text']).swapcase()
        return render(
            request,
            'text_change.html',
            {'text': request_data}
        )


def hw_text_swap(request: WSGIRequest):
    end_result = 'Here will be your text'
    if request.method == 'POST':
        request_data= str(dict(request.POST.items())['text', 'no text'])