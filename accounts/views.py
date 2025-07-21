from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/home.html')

def dash_view(request):
    users = User.objects.all()
    return render(request, 'accounts/dash.html', {'users': users})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "login successful.")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('dash')
    
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "User updated successfully.")
        return redirect('dash')
    
    return render(request, 'accounts/update.html', {'user': user})

# def update_user(request, pk):
#     return render(request, 'accounts/update.html', {'pk': pk})


def info_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Information successful.")
            return redirect('dash')
    else:
        form = RegisterForm()
    return render(request, 'accounts/list.html', {'form': form})
