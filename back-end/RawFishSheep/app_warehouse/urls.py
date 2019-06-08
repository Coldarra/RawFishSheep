from django.urls import path, include
from . import server

urlpatterns = [
    path("", server.test),
    path("all", server.get_warehouseinfo),
    path("append", server.append_warehouse),
    path("setting", server.modify_warehouse),
    path("delete", server.delete_warehouse),
    path("cargoin/", include([
        path("info", server.get_cargoin_info),
        path("append", server.append_cargoin),
        path("delete", server.delete_cargoin),
    ])),
    path("cargoout/", include([
        path("info", server.get_cargoout_info),
        path("append", server.append_cargoout),
        path("delete", server.delete_cargoout),
    ])),
]
