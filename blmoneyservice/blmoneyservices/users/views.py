from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Client
from blmoneyservices import *


# from .RegisterForm import RegisterForm


# Create your views here.
def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        u = Client(name=username, password=password)
        u.save()
        # messages.add_message(request, messages.SUCCESS, "Successfully logged in")
        return redirect(gohome)
    return render(request, 'users/register.html', {'form': form})


def gohome(request):
    context = {}
    return render(request, 'users/home.html', context)


def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)
