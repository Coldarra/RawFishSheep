from django.urls import path, include
from . import views
from . import server
from decorator import *

urlpatterns = [
    path("all", server.cart_all),
    path("append",server.append_cart),
    path("delete",server.delete_cart),
    path("updateamount",server.cart_update_amount),
    path("updatestatue",server.cart_update_state),

]
