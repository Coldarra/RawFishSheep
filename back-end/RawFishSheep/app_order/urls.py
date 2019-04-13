from django.urls import path, include
from . import views

urlpatterns = [
    path("all/",views.order_all),
    path("all/unfinished/",views.order_unfinished),
    path("append/",views.order_append),
    path("all/finished/",views.order_finished),

]
