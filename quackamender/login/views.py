from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.




def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")






def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            return render(request, "signup.html", {"error": "Passwords do not match"})
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})
        user = User.objects.create(username=username, password=make_password(password))
        user.save()
        return HttpResponseRedirect(reverse("login"))
    return render(request, "signup.html")