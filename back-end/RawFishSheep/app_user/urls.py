from django.urls import path, include
from . import views
from . import server
from decorator import *


class Interface():
    def __init__(self, interface="null", request=None):
        self.interface = interface
        self.request = request
        # self.params = params

    def get(func):
        def wrapper(request, *args, **kw):
            print('call %s():' % func.__name__)
            print(request)
            if request.method != "GET":
                return pack("method", "100", "接口调用方式错误")
            return func(request, *args, **kw)
        return wrapper


class UserInterface():
    @get
    def interface_test(request):
        print()
        for key, value in request.GET.lists():
            print(key, value)
        for key, value in request.POST.lists():
            print(key, value)
        interface_id = "test"
        resp = views.test(interface_id, "ok")
        return pack(interface_id, data=resp)

    def decodeToken(request):
        interface_id = "token"
        token = request.META.get("HTTP_AUTHORIZATION", None)
        token_data = verifyToken(token)
        if token_data:
            return pack(interface_id, data={"user": token_data, "token": token})
        else:
            return pack(interface_id, "token_verify_fail", "无效token, 请重新登录")


urlpatterns = [
    path("", UserInterface.interface_test),
    path("token", views.decodeToken),
    path("login", server.log_in),
    path("logout", views.log_out),
    path("register", views.register),
    path("info", views.userinfo),
    path("checklogin", views.checklogin),
    path("setting", views.changeinfo),
    path("delete", views.delete_account),
    path("address/", include([
        path("all", views.get_address),
        path("append", views.append_address),
        path("default", views.default_address),
        path("delete", views.delete_address),
    ])),

]
