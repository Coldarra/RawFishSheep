from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("info", views.info),
    path("append", views.append),
    path("setting", views.setting),
    path("delete", views.delete),
]
