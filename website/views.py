from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')

    return render(request, 'home.html',{})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            return render(request, 'home.html', {})


def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

def register_user(request):
     return render(request, 'register.html', {})
