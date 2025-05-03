from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if "logout" in request.GET:
        logout(request)
        return HttpResponseRedirect(reverse("login"))
    if request.user.is_authenticated:
        return render(request, "index.html",{ "user": request.user.username})
    else:
        return HttpResponseRedirect(reverse("login"))
    

    
