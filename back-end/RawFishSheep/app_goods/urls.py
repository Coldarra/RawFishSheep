from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.test),
    path("info", views.info),
    path("append", views.append),
    path("setting", views.setting),
    path("delete", views.delete),
    path("category/", include([
        path("all", views.get_category),
        path("append", views.append_category),
        path("setting", views.setting_category),
    ])),
]
