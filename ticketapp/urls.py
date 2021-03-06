from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name = "register"),
    path("login_view", views.login_view, name="login_view"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("logout_page", views.logout_page, name="logout_page")
]