from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import Client



# from .RegisterForm import RegisterForm


# Create your views here.
def registerPage(request):
    # form = UserCreationForm()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        u = Client(username=username, email=email, password=password)
        u.save()
        # messages.add_message(request, messages.SUCCESS, "Successfully logged in")
        return redirect(gohome)
    return render(request, 'users/register.html')



def gohome(request):
    context = {}
    return render(request, 'users/home.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        
        client = auth.authenticate(username=username, password1=password1)
        
        if client is not None:
            auth.login(request, client)
            return redirect(gohome)
        else:
            messages.info(request, 'Invalid username or password')
            return redirect(registerPage)
    else:
        return render(request, 'users/login.html')
