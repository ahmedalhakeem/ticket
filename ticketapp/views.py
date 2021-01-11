from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import *
from django import forms
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return HttpResponseRedirect('admin')
        if request.user.groups.filter(id=2).exists():
            return render(request, "ticketapp/employee.html")
        if request.user.groups.filter(id=1).exists():
            return render(request, "ticketapp/it.html")
    return render(request, "ticketapp/index.html")
#####
def login_view(request):
    if request.method == "POST":

        username = request.POST['username1']
        password = request.POST['password1']
        print(username)
        print(password)
        #user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None: 
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ticketapp/login_view.html",{
                "message": "Invalid Username/Password"
            })

    else:
        return render(request, "ticketapp/login_view.html")
####
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":

        new_user = UserForm(request.POST or None)
        if new_user.is_valid():
            first_name= new_user.cleaned_data["first_name"]
            last_name= new_user.cleaned_data["last_name"]
            username = new_user.cleaned_data["username"]
            email = new_user.cleaned_data["email"]
            password = new_user.cleaned_data["password"]
            pc_code = new_user.cleaned_data["pc_code"]
            department = new_user.cleaned_data["deptartment"]
            section = new_user.cleaned_data["section"]
            
            # Check if the user is already exists:
            try:
                #user = User(first_name=first_name, last_name=last_name, username = username, email=email, password=password, deptartment=department, section=section)
                user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password, deptartment=department, section=section, pc_code=pc_code)
                if user.section == 'IT':
                    user.groups.add(1)
                else:
                    user.groups.add(2)
                user.save()
            except IntegrityError:
                return render(request, "ticketapp/register.html", {
                    "message" : "username already taken"
                })
            login(request, user)
        
        return HttpResponseRedirect(reverse("index"))
    else:
        new_user=UserForm()

        return render(request, "ticketapp/register.html",{
            "new_user" : new_user
    })

@login_required    
def it(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, "ticketapp/it.html",{
        "user" : user
    })
@login_required
def employee(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "ticketapp/employee.html",{
        "user": user
    })