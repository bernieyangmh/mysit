# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
@csrf_protect
def user_login(request):
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = password = ''
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                login(request, user)
                return diff_response(request)
            else:
                return diff_response(request)
    form = AuthenticationForm()
    ctx = {}
    ctx.update({'request': request})
    ctx['form'] = form
    return render(request, 'login.html', ctx)

def user_logout(request):
    logout(request)
    return redirect('/users')


def diff_response(request):
    if request.user.is_authenticated():
        content = "<p>my dear user<p>"
    else:
        content = "<p>you wired stranger</p>"
    return HttpResponse(content)

def first_page(request):
    return HttpResponse("<p>用户</p>")

@login_required
def user_only(request):
    return HttpResponse("<p>This message is for logged is user only")

def name_check(user):
    return user.get_username() == 'bernie001'


#The parameter of decorators must be True
@user_passes_test(name_check)
def specific_user(request):
    return HttpResponse("<p>for bernie only<p>")

def is_login(request):
    return render(request, 'is_login.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return redirect("/users")
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(request)
        return render(request, "register.html", ctx)
