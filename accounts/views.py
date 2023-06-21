from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    template = loader.get_template('accounts/login.html')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request=request, user=user)
            return redirect('/overview')
        else:
            messages.success(request, ('Login not successful.'))

    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def logout_view(request):
    context = {}
    if request.method == 'POST':
        logout(request)
        redirect('/login')
    template = loader.get_template('accounts/logout.html')
    return HttpResponse(template.render(context, request))


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login')

    context = {
        "form": form
    }
    template = loader.get_template('accounts/register.html')
    return HttpResponse(template.render(context, request))
