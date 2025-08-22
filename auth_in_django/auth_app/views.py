from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully!")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match")
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}, you are logged in!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("login")

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")
