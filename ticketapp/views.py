from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

def index(request):
    return render(request, "ticketapp/index.html")

def login_page(request):
    if request.method == "POST":

        username= request.POST["username"]
        password = request.POST["password"]
        user = authenticate( username = username, password= password)
        print(user)
        if user is not None:
            if user.is_active:
                
                login(request, user)
            
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "ticketapp/login_page.html",{
                    "message1": "User is not active"
                })
        else:
            return render(request, "ticketapp/login_page.html",{
                "message2" : "Invalid Username/Password"
            })
    else:
        return render(request, "ticketapp/login_page.html")

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
                user = User(first_name=first_name, last_name=last_name, username = username, email=email, password=password, deptartment=department, section=section)
                

                user.save()
            except IntegrityError:
                return render(request, "ticketapp/register.html", {
                    "message" : "username already exists"
                })
        login(request, user )
        return HttpResponseRedirect(reverse("index"))
    else:

        return render(request, "ticketapp/register.html",{
            "new_user" : UserForm()
    })

@login_required    
def profile(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, "ticketapp/user_profile.html",{
        "user" : user
    })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
