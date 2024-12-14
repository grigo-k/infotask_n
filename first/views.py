from django.shortcuts import render
from datetime import datetime

from django.template.context_processors import request


def index(request):
    context = {
        "title" : 'Курс "Промышленное программирование"',
        "name": 'LMAO',
        "count_page" : 3
    }

    return render(request, 'index_page.html', context)


def calc(request):
    #/?a=3&b=8
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    context = {
        "title": 'Курс "Промышленное программирование"',
        "a" : a,
        "b" : b,
        "sum" : a+b
    }

    return render(request, 'calc_page.html', context)


def time(request):
    date = datetime.now().strftime("%d/%m/%Y")
    time_n = datetime.now().strftime("%H/%M/%S")
    context = {
        "title": 'Курс "Промышленное программирование"',
        "current_date" : date,
        "current_time" : time_n
    }

    return render(request, 'time_page.html', context)