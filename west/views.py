
# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse
from west.models import Character

def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs': staff_list})

def first_page(request):
    return HttpResponse("<p>西餐</p>")

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')

@csrf_protect
def investigate(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['staff']
    return render(request, "investigate.html", ctx)