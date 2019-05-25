from django.urls import path, include
from . import views
from . import server
from decorator import *

urlpatterns = [
    path("", views.test),
    path("all/",server.order_all),
    path("unfinished/",server.order_unfinished),
    path("append/",server.order_append),
    path("finished/",server.order_finished),
    path("info/",server.order_info),
    path("makefinished/",server.order_finished),
    path("delete/",server.order_delete),



]
