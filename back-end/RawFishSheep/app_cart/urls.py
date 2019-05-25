from django.urls import path, include
from . import views
from . import server
from decorator import *

urlpatterns = [
    path("all/", server.get_all_cart),
    path("append/",server.append_cart),
    path("delete/",server.delete_cart),
    path("updateamount/",server.update_amount),
    path("updatestatue/",server.update_state),

]
