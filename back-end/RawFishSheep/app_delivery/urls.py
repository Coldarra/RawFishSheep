from django.urls import path, include
from . import server

urlpatterns = [
    path("undistribution", server.get_undistribution),
    path("audit", server.audit_order),
    path("distribution", server.distribut_order),
    path("receive", server.receive_order),
    path("finish", server.finish_order),
]