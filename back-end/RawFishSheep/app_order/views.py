from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import datetime
import time
import random
from decorator import *
from app_cart.views import *
from .models import *


def getOrderByUser(user_id=None, mode="all"):
    if user_id == None:
        raise ParamException()
    if mode == "all":
        orders = Order.objects.filter(
            user_id=user_id, isdelete='0').order_by("-id")
    elif mode == "unfinished":
        orders = Order.objects.filter(
            user_id=user_id, isdelete='0', status__in=['processing', 'examining', 'preparing', 'delivering', 'delivered'])
    elif mode == "finished":
        orders = Order.objects.filter(
            user_id=user_id, isdelete='0', status='confirmed')
    return orders


def getOrderByMode(mode=None):
    print(mode)
    if mode == None:
        raise ParamException()
    elif mode not in ['unprocessed', 'processing', 'examining', 'preparing', 'delivering', 'delivered', 'confirmed', 'all']:
        raise ParamException()
    elif mode == "all":
        orders = Order.objects.filter(isdelete='0')
    else:
        orders = Order.objects.filter(isdelete='0', status=mode)
    return orders


def getOrderByID(order_id=None, serialnumber=None):
    if order_id == None and serialnumber == None:
        raise ParamException()
    if order_id:
        if Order.objects.filter(isdelete='0', id=order_id).count() == 1:
            return Order.objects.get(isdelete='0', id=order_id)
        raise RFSException('50012', '无效订单')
    elif serialnumber:
        if Order.objects.filter(isdelete='0', serialnumber=serialnumber).count() == 1:
            return Order.objects.get(isdelete='0', serialnumber=serialnumber)
        raise RFSException('50012', '无效订单')
    raise ParamException()


def createOrder(user_id=None, discount=1, paymentname=None, address_id=None):
    if None in [user_id, discount, paymentname, address_id]:
        raise ParamException()
    carts = getSelectedCart(user_id)
    if len(carts) == 0:
        raise RFSException('50112', '未选择任何商品或购物车为空')
    totalprice = 0
    for cart in carts:
        if cart.goods.remain < cart.amount:
            raise RFSException('50111', '商品余量不足')
        totalprice = totalprice + cart.goods.price * cart.amount * discount

    # 创建订单表
    serialnumber = "{}{}{}".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                                   int(time.time()*1000),
                                   random.randint(1000, 9999))

    order = Order.objects.create(
        user_id=user_id,
        address_id=address_id,
        totalprice=int(totalprice),
        discount=discount,
        createtime=datetime.datetime.now(),
        paymentname=paymentname
    )
    # 创建订单详情表
    for cart in carts:
        createOrderDetail(order.id, cart.goods_id,
                          cart.goods.price, cart.amount)
    deleteSelectedCart(user_id)
    return order


def paidOrder(order_id=None):
    pass


def changeOrder(order_id=None, mode=None):
    if None in [order_id, mode]:
        raise ParamException()
    if mode not in ['processing', 'examining', 'preparing', 'delivering', 'delivered', 'unprocessed']:
        raise RFSException('50213', '订单状态非法')
    order = getOrderByID(order_id)
    # 检验当前状态是否正确
    if order.status == 'processing' and mode == "processing":
        order.status = 'examining'
    elif order.status == 'examining' and mode == "examining":
        order.status = 'preparing'
    elif order.status == 'preparing' and mode == "preparing":
        order.status = 'delivering'
    elif order.status == 'delivering' and mode == "delivering":
        order.status = 'delivered'
    elif order.status == 'delivered' and mode == "delivered":
        order.status = 'confirmed'
    elif order.status == 'unprocessed' and mode == "unprocessed":
        order.status = 'processing'
    else:
        raise RFSException('50213', '订单状态非法')
    order.save()


def createOrderDetail(order_id=None, goods_id=None, price=None, amount=None):
    if None in [order_id, goods_id, price, amount]:
        raise ParamException()
    return OrderDetail.objects.create(
        order_id=order_id, goods_id=goods_id, price=int(price), amount=amount)


def deleteOrder(order_id=None):
    if order_id == None:
        raise ParamException()
    order = getOrderByID(order_id)
    if order_obj.status in['processing', 'examining', 'confirmed']:
        order.isdelete = '1'
        order.save()
    else:
        raise RFSException("50301", "删除失败")
