from django.urls import path, include
from . import views
from . import server
from decorator import *

urlpatterns = [
    path("", server.get_all_order),
    path("all", server.get_all_order),
    path("unfinished", server.get_unfinished_order),
    path("append", server.append_order),
    path("finished", server.get_finished_order),
    path("info", server.get_order_info),
    path("confirm", server.confirm_order),
    path("delete", server.delete_order),

    path("delivery/", include([
        path("", server.get_delivery_info),
        path("info", server.get_delivery_info),
        # path("append", server.append_address),
    ])),

]
