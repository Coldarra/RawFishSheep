from django.urls import path, include
from . import views

urlpatterns = [
    path("all/",views.order_all),
    path("cart/all/",views.cart_all),
    path("cart/append/",views.cart_append),
    path("",views.test),
    path("cart/delete/",views.cart_delete),
    path("cart/updatestate/",views.cart_update_state),
    path("cart/updateamount/",views.cart_update_amount),

]
