from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("undistribution", views.undistribution),
    path("distribution", views.distribution),
    path("finish", views.finish),
]