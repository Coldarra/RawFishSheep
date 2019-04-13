from django.urls import path, include
from . import views

urlpatterns = [
    path("all/",views.order_all),
    path("",views.test),

]
