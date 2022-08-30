from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Client



# from .RegisterForm import RegisterForm


# Create your views here.
def registerPage(request):
    pass


def gohome(request):
    context = {}
    return render(request, 'users/home.html', context)


def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)
