from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("info", views.info),
    # path("append", views.append)
]
