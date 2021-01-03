from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    return render(request, "ticketapp/index.html")

def register(request):

    
    new_user = UserForm(request.POST or None)
    if new_user.is_valid():
        first_name= new_user.cleaned_data["first_name"]
        last_name= new_user.cleaned_data["last_name"]
        email = new_user.cleaned_data["email"]
        password = new_user.cleaned_data["password"]
        pc_code = new_user.cleaned_data["pc_code"]
        department = new_user.cleaned_data["deptartment"]
        section = new_user.cleaned_data["section"]
    
    return render(request, "ticketapp/register.html",{
        "new_user" : UserForm()
    })