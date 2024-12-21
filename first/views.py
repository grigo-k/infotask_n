from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from random import randint
from first.models import RandomHistory
from first.forms import CommentForm

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
    exp = ""
    for i in range(n):
        nums.append(randint(10, 99))
    r = nums[0]
    exp += str(nums[0])
    for i in range(1, n):
        op = randint(1, 2)

        if op == 1:
            r += nums[i]
            exp += " + " + str(nums[i])
        else:
            r -= nums[i]
            exp += " - " + str(nums[i])

    exp += " = " + str(r)

    historyr = RandomHistory(text=str(exp), created_date=datetime.now())
    historyr.save()

    context = {
        "title": 'Курс "Промышленное программирование"',
        "exp" : exp
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
        "name" : "History cleared"
    }

    return render(request, 'clear_page.html', context)

def delete(request):
    if RandomHistory.objects.exists():
        RandomHistory.objects.last().delete()
        context = {
            "title": 'Курс "Промышленное программирование"',
            "name": "Last expression cleared"
        }
    else:
        context = {
            "title": 'Курс "Промышленное программирование"',
            "name": "No objects to delete"
        }

    return render(request, 'delete_page.html', context)

def new(request):
    if "text" in request.POST:
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            text = comment_form.cleaned_data["text"]

        text = request.POST.get("text", "Empty")

        num_n = 0
        num = "0"
        next_a = "+"
        new_text = ""
        for i in text:
            if i.isdigit():
                num += i
                new_text += i
            elif i == "+" or i == "-":
                if int(num) != 0:
                    if next_a == "+":
                        num_n += int(num)
                    else:
                        num_n -= int(num)
                    next_a = i
                    num = "0"
                    new_text += f" {i} "
            else:
                pass
        if next_a == "+":
            num_n += int(num)
        else:
            num_n -= int(num)

        historyr = RandomHistory(text=str(new_text + " = " + str(num_n)), created_date=datetime.now())
        historyr.save()
        return HttpResponseRedirect('/history/')
    else:
        comment_form = CommentForm()
    context = {
        "title": 'Курс "Промышленное программирование"',
        "comment_form" : comment_form
    }

    return render(request, 'new_page.html', context)