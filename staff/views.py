# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from .forms import SignUpForm, LoginForm


def staff_login(request):

    if not request.user.is_anonymous():
        return redirect(settings.LOGIN_REDIRECT_URL)

    context = {
        'form': LoginForm(request.POST or None),
        'is_login_layout': True
    }

    if request.POST:
        #import pdb; pdb.set_trace()
        if context['form'].is_valid():
            user_dj = User.objects.filter(username=context['form'].data['username'])
            if user_dj:
                access_registry = authenticate(username=context['form'].data['username'],
                                               password=context['form'].data['password'])
                if access_registry is not None:
                    login(request, access_registry)
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    context['message_errors'] = 'Wrong Credentials, verify username and password'
            else:
                context['message_errors'] = 'User Doesn\'t Exist'
        else:
            context['message_errors'] = context['form'].errors

    return render(request, 'login.html', context)


def staff_signup(request):
    context = {
        'form': SignUpForm(request.POST or None),
        'is_login_layout': True
    }

    if request.POST:
        if context['form'].is_valid():
            new_user = context['form'].save()
            new_user.set_password(context['form'].data['password'])
            new_user.save()
            access_registry = authenticate(username=context['form'].data['username'],
                                           password=context['form'].data['password'])
            login(request, access_registry)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            context['message_errors'] = context['form'].errors
    return render(request, 'signup.html', context)


@login_required(login_url=settings.LOGIN_URL)
def staff_logout(request):
    logout(request)
    return redirect('staff_login')


@login_required(login_url=settings.LOGIN_URL)
def staff_home(request):
    return render(request, 'home.html', {})

