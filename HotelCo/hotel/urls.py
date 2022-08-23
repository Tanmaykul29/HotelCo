from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("option", views.option, name="option"),
    path("focus/<int:id>", views.focus, name="focus"),
    path("booking", views.booking, name="userinfo"),
]