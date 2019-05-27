from .models import *
from app_order.views import *
from app_user.views import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def createDelivery(user_id=None, order_id=None):
    if None in [user_id, order_id]:
        raise ParamException()
    user = getUserByID(user_id)
    order = getOrderByID(order_id)
    delivery = Delivery.objects.create(
        order=order,
        user=user,
        receivetime=datetime.datetime.now(),
    )


def finishDelivery(order_id):
    if order_id == None:
        raise ParamException()
    delivery = getDeliverByOrder(order_id)
    delivery.finishtime = datetime.datetime.now()
    delivery.save()


def getDeliverByOrder(order_id=None):
    if order_id == None:
        raise ParamException()
    if Delivery.objects.filter(isdelete="0").count():
        return Delivery.objects.get(order_id=order_id)
    else:
        raise RFSException("60101", "无此订单")


def changeDelivery(user_id=None, order_id=None, mode=None):
    if None in [order_id, mode]:
        raise ParamException()
    if mode == "preparing" and user_id == None:
        raise ParamException()
    if mode == "preparing":
        user = getUserByID(user_id)
        if user.level not in ["courier"]:
            raise RFSException("60112", "无效用户")
        createDelivery(user_id, order_id)
    elif mode == "delivering":
        finishDelivery(order_id)
    changeOrder(order_id, mode)