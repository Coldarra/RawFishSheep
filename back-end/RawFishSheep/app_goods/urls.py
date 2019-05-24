from django.urls import path, include
from . import views
from . import server

urlpatterns = [
    path("all", server.get_all_goods),
    path("info", server.get_goods_info),
    path("append", server.create_goods),
    path("setting", server.change_goods),
    path("delete", server.delete_goods),
    path("category/", include([
        path("all", server.get_category),
        path("append", server.append_category),
        path("setting", server.setting_category),
        path("delete", server.delete_category)
    ])),
    path("picture/", include([
        path("all", server.get_picture),
        # path("append", server.append_picture),
        path("delete", server.delete_picture)
    ])),
]
