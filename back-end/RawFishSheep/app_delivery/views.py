from .models import *
from app_order.views import *
from app_user.views import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def createDelivery(user_id=None, order_id=None):
    if None in [user_id, order_id]:
        raise ParamException()
    if Delivery.objects.filter(isdelete="0", order_id=order.id).count() == 1:
        raise RFSException("50211", "该订单已有配送单")
    delivery = Delivery.objects.create(
        order_id=order_id,
        user_id=user_id,
        receivetime=datetime.datetime.now(),
    )


def finishDelivery(order_id):
    if order_id == None:
        raise ParamException()
    delivery = getDeliverByOrder(order_id)
    delivery.finishtime = datetime.datetime.now()
    delivery.save()


def getDeliverByOrder(order_id=None, serialnumber=None):
    if order_id == None and serialnumber == None:
        raise ParamException()
    if order_id:
        if Delivery.objects.filter(isdelete="0", order_id=order_id).count():
            return Delivery.objects.get(isdelete="0", order_id=order_id)
    elif serialnumber:
        order = getOrderByID(order_id, serialnumber)
        if Delivery.objects.filter(isdelete="0", order_id=order.id).count() == 1:
            return Delivery.objects.get(isdelete="0", order_id=order.id)
        else:
            raise RFSException("60101", "当前订单暂无配送信息")
    else:
        raise RFSException("60102", "无此配送单")


def setDeliveryInfo(user_id=None, order_id=None, mode=None):
    if None in [order_id, mode]:
        raise ParamException()
    if mode == "preparing" and user_id == None:
        raise ParamException()
    if mode == "preparing":
        user = getUserByID(user_id)
        if user.level not in ["courier", "admin"]:
            raise RFSException("60112", "无效用户")
        createDelivery(user_id, order_id)
    elif mode == "delivering":
        finishDelivery(order_id)
    changeOrder(order_id, mode)
