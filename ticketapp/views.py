from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    return render(request, "ticketapp/index.html")

def register(request):
    
    new_user = UserForm()
    return render(request, "ticketapp/register.html",{
        "userForm": UserForm()
    })