from django.urls import path, include
from . import views

urlpatterns = [
    path("all/",views.order_all),
    path("unfinished/",views.order_unfinished),
    path("append/",views.order_append),
    path("finished/",views.order_finished),

]
