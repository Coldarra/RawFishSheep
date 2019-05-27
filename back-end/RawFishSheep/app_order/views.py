from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import datetime
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
    elif mode not in ['unprocessed','processing', 'examining', 'preparing', 'delivering', 'delivered', 'confirmed', 'all']:
        raise ParamException()
    elif mode == "all":
        orders = Order.objects.filter(isdelete='0')
    else:
        orders = Order.objects.filter(isdelete='0', status=mode)
    return orders


def getOrderByID(order_id=None):
    if order_id == None:
        raise ParamException()
    try:
        return Order.objects.get(isdelete='0', id=order_id)
    except:
        raise RFSException('50012', '无效订单')


def createOrder(user_id=None, discount=1, paymentname=None, address_id=None):
    if None in [user_id, level, paymentname, address_id]:
        raise ParamException()
    carts = getCartList(user_id)
    # 计算totalprice和输入时间
    totalprice = 0
    for cart in carts:
        if cart.goods.remain < cart.amount:
            raise RFSException('50111', '商品余量不足')
        totalprice = totalprice + cart.goods.price * cart.amount * discount
    # 创建订单表
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
        createOrderDetail(order.id, cart.goods_id, price, cart.amount)
    return order


def paidOrder(order_id=None):
    pass


def changeOrder(order_id=None, mode=None):
    if order_id == None:
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
    order.save()


def createOrderDetail(order_id=None, goods_id=None, price=None, amount=None):
    if None in [order_id, goods_id, price, amount]:
        raise ParamException()
    return OrderDetail.objects.create(
        order=order_row, goods_id=cart.goods.id, price=int(cart.goods.price), amount=cart.amount)


def deleteOrder(order_id=None):
    if order_id == None:
        raise ParamException()
    order = getOrderByID(order_id)
    if order_obj.status in['processing', 'examining', 'confirmed']:
        order.isdelete = '1'
        order.save()
    else:
        raise RFSException("50301", "删除失败")
