
# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from west.models import Character

def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    context = {'label': ' '.join(staff_str)}
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")


def first_page(request):
    return HttpResponse("<p>西餐</p>")

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)