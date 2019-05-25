from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import datetime
from decorator import *
from app_cart.views import *
from .models import *
# Create your views here.

# 查询当前用户所有的购物车信息


def test(param):
    # status_mapping = {"0": "processing",
    #                   "1": "examining",
    #                   "2": "preparing",
    #                   "3": "delivering",
    #                   "4": "delivered",
    #                   "5": "confirmed", }
    # for order in Order.objects.all():
    #     order.status = status_mapping.get(order.status, "error")
    #     order.save()
    return pack()

def get_All(user_id):

    # 查找当前用户的所有订单及订单详情
    try:
        order_obj = Order.objects.filter(
            user_id=user_id, isdelete='0').order_by("-id")
    # 生成所有的
    except:
        raise RFSException("50001","查询订单失败")
    resp = {'order': [order.toDict() for order in order_obj]}
    return resp

def get_unfinished(user_id):
    # 查找当前用户的所有未完成订单及订单详情
    try:
        orders_obj = Order.objects.filter(
            user_id=user_id, isdelete='0', status__in=['processing', 'examining', 'preparing', 'delivering','delivered'])
    except:
        raise RFSException("50011","查询订单失败")
    resp = {'order': [order.toDict() for order in orders_obj]}
    return resp

def get_finished(user_id):
    # 查找当前用户的所有完成订单及订单详情
    try:
        orders_obj = Order.objects.filter(user_id=user_id, isdelete='0', status='confirmed')
    except:
        raise RFSException("50021","查询订单失败")
    resp = {'order': [order.toDict() for order in orders_obj]}
    return resp

def get_info(user_id,order_id):
    interface_id = '5010'
    try:
        order_obj = Order.objects.get(user_id=user_id, isdelete='0', id=order_id)
    except:
        raise RFSException('50012', '无效订单')
    # 生成所有的
    resp = {'order': order_obj.toDict()}
    return resp

def append_order(user_id,level,paymentname,address_id):
    # 设置折扣值
    if level == 'vip':
        discount = 0.9
    else:
        discount = 1
    cart_obj = get_cartlist(user_id)
    # 计算totalprice和输入时间
    totalprice = 0
    for cart_each in cart_obj:
        try:
            cart_each.goods_id
        except:
            raise RFSException('50112', '无效商品')
        if cart_each.goods.remain < cart_each.amount:
            cart_each.amount = cart_each.goods.remain
            raise RFSException('50111', '商品数量不够')
        totalprice = totalprice + cart_each.goods.price * cart_each.amount * discount
    createtime = datetime.datetime.now()
    # 创建订单表
    order_row = Order.objects.create(
        user_id=user_id,
        address_id=address_id,
        totalprice=int(totalprice),
        discount=discount,
        createtime=createtime,
        paymentname=paymentname
    )
    # 创建订单详情表
    for cart_each in cart_obj:
        price = cart_each.goods.price*cart_each.amount*discount
        amount = cart_each.amount
        order_detail_row = OrderDetail.objects.create(
            order=order_row, goods_id=cart_each.goods.id, price=price,amount = amount)
    # 创建返回值
    order_data = order_row.toDict()
    resp = {'order': order_data}
    return resp

def make_finished(order_id):
    # 检验订单是否有效
    try:
        order_obj = Order.objects.get(id = order_id)
    except:
        raise RFSException('50212', '无效订单')
    # 检验当前状态是否为‘4’
    if order_obj.status == 'delivered':
        order_obj.status = 'confirmed'
        order_obj.save()
    else:
        raise RFSException('50213', '订单状态非法')

def delete_order(user_id):
    try:
        order_obj = Order.objects.filter(user_id = user_id)
        for order in order_obj:
            order.isdelete = '1'
            order.save()
    except:
         raise RFSException("50301","删除失败")
    
    

