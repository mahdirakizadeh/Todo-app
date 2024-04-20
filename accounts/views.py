from django.shortcuts import render, redirect
from .forms import UserRegistrationFrom, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def User_register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, "your sign in is successfully", 'success')
            return redirect('home')
    else:
        form = UserRegistrationFrom()
    return render(request, 'register.html', {'form': form})


def User_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "your login is successfully", 'success')
                return redirect('home')
            else:
                messages.success(request, "your username or password is invalid", 'danger')
                return render(request, 'login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


def User_logout(request):
    logout(request)
    messages.success(request, "your logout is successfully", 'success')
    return redirect('home')
