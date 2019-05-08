from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("token", views.decodeToken),
    path("login", views.log_in),
    path("logout", views.log_out),
    path("register", views.register),
    path("info", views.userinfo),
    path("checklogin", views.checklogin),
    path("setting", views.changeinfo),
    path("delete", views.delete_account),
    path("address/", include([
        path("all", views.get_address),
        path("append", views.append_address),
        path("default", views.default_address),
        path("delete", views.delete_address),
    ])),
    
]
