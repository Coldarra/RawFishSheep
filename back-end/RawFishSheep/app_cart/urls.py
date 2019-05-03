from django.urls import path, include
from . import views

urlpatterns = [
    path("all",views.cart_all),
    path("append",views.cart_append),
    path("delete",views.cart_delete),
    path("updatestate",views.cart_update_state),
    path("updateamount",views.cart_update_amount),

]
