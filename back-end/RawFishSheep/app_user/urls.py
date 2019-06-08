from django.urls import path, include
from . import views
from . import server
from decorator import *


urlpatterns = [
    path("", server.test),
    path("token", server.decodeToken),
    path("login", server.log_in),
    path("logout", server.log_out),
    path("register", server.register),
    path("info", server.userinfo),
    path("setting", server.set_userinfo),
    path("delete", server.delete_account),
    path("address/", include([
        path("all", server.get_address),
        path("append", server.append_address),
        path("default", server.default_address),
        path("delete", server.delete_address),
    ])),

]
