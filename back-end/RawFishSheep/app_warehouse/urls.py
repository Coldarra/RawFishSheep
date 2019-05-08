from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.test),
    path("all",views.get_warehouseinfo),
    path("append",views.append_warehouse),
    path("setting", views.modify_address),
    path("delete", views.delete_address),
    path("cargoin/", include([
        path("info", views.get_cargoin_info),
        path("append", views.append_cargoin),
        path("delete", views.get_cargoin_info),
    ])),
    path("cargoout/", include([
        path("info", views.get_cargoin_info),
        path("append", views.get_cargoin_info),
        path("delete", views.get_cargoin_info),
    ])),
]
