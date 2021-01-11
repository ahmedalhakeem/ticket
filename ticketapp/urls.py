from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name = "register"),
    path("login_view", views.login_view, name="login_view"),
    path("it/<int:user_id>", views.it, name="profile"),
    path("employee/<int:user_id", views.employee, name="employee"),
    path("logout_page", views.logout_page, name="logout_page"),
    path('admin', admin.site.urls)
]