from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("login", views.log_in),
    path("logout", views.log_out),
    path("register", views.register),
]
