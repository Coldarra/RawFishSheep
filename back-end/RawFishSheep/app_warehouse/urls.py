from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.test),
    path("all",views.get_warehouseinfo),
    path("append",views.append_warehouse),
    path("delete",views.modify_address),
]
