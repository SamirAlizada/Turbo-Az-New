from django.shortcuts import redirect, render
from .models import User
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    
    context = {
        'form' : form
    }

    return render(request, 'register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form' : form
    }

    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')