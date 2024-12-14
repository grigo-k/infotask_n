from django.shortcuts import render
from datetime import datetime
from random import randint
from first.models import RandomHistory

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

def expression(request):
    n = randint(2, 4)
    nums = []
    for i in range(n):
        nums.append(randint(10, 99))
    r = nums[0]
    for i in range(1, n):
        op = randint(1, 2)
        if op == 1:
            r += nums[i]
        else:
            r -= nums[i]

    historyr = RandomHistory(text=str(r), created_date=datetime.now())
    historyr.save()

    context = {
        "title": 'Курс "Промышленное программирование"',
        "R" : r
    }

    return render(request, 'expression_page.html', context)


def history(request):
    rand_history = RandomHistory.objects.all()
    context = {
        "title": 'Курс "Промышленное программирование"',
        "rand_history": rand_history
    }

    return render(request, 'history_page.html', context)

def clear(request):
    RandomHistory.objects.all().delete()
    context = {
        "title": 'Курс "Промышленное программирование"',
        "name" : "BOOM"
    }

    return render(request, 'clear.html', context)