from django.urls import path, include
from . import views
from . import server
from decorator import *

urlpatterns = [
    path("", views.test),
    path("all/",server.get_all_order),
    path("unfinished/",server.get_unfinished_order),
    path("append/",server.append_order),
    path("finished/",server.get_finished_order),
    path("info/",server.get_order_info),
    path("makefinished/",server.make_order_finished),
    path("delete/",server.delete_order),



]
