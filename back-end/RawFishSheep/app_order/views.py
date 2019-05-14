from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import datetime
from decorator import *

from .models import *
# Create your views here.

#查询当前用户所有的购物车信息
@login
@get
def order_all(request):
    interface_id = '5000'
    user_id = request.session['userid']
    #查找当前用户的所有订单及订单详情
    orders = Order.objects.filter(user_id = user_id,isdelete='0')
    order_result = []
    for order in orders:
        ord_detail_list = []
        ord_mid = order.toDict()
        details = order.detail_by_order.filter(isdelete='0')
        for deta in details:
            ord_detail_list.append(deta.toDict())
        ord_mid['order_detial'] = ord_detail_list
        order_result.append(ord_mid)
    #生成所有的
    resp = {'data':order_result}
    return pack(interface_id,data = resp)
   
@login
@get
def order_unfinished(request):
    interface_id = '5001'
    user_id = request.session['userid']
    #查找当前用户的所有未完成订单及订单详情
    orders = Order.objects.filter(user_id = user_id,isdelete='0', status__in=['1','2','3','4'])
    order_result = []
    for order in orders:
        ord_detail_list = []
        ord_mid = order.toDict()
        details = order.detail_by_order.filter(isdelete='0')
        for deta in details:
            ord_detail_list.append(deta.toDict())
        ord_mid['order_detial'] = ord_detail_list
        order_result.append(ord_mid)
    #生成返回值
    resp = {'data':order_result}
    return pack(interface_id,data = resp)

@login
@get
def order_finished(request):
    interface_id = '5001'
    user_id = request.session['userid']
    #查找当前用户的所有完成订单及订单详情
    orders = Order.objects.filter(user_id = user_id,isdelete='0', status = '5')
    order_result = []
    for order in orders:
        ord_detail_list = []
        ord_mid = order.toDict()
        details = order.detail_by_order.filter(isdelete='0')
        for deta in details:
            ord_detail_list.append(deta.toDict())
        ord_mid['order_detial'] = ord_detail_list
        order_result.append(ord_mid)
    #生成返回值
    resp = {'data':order_result}
    return pack(interface_id,data = resp)

@login
@get
def order_info(request):
    interface_id = '5010'
    user_id = request.session['userid']
    orderid = request.GET.get('order_id',None)
    #根据orderid查找当前用户的单个订单及订单详情
    try:
        order = Order.objects.get(user_id = user_id,isdelete='0',id= orderid)
    except:
        return pack(interface_id,'50012','无效订单')
    order_result = []
    ord_detail_list = []
    ord_mid = order.toDict()
    details = order.detail_by_order.filter(isdelete='0')
    for deta in details:
        ord_detail_list.append(deta.toDict())
    ord_mid['order_detial'] = ord_detail_list
    order_result.append(ord_mid)
    #生成所有的
    resp = {'data':order_result}
    return pack(interface_id,data = resp)


@login
@post
def order_append(request):
    interface_id = '5011'
    goods_mid = []
    user_id = request.session['userid']
    #设置折扣值
    if request.session['level']=='vip':
        discount = 0.9
    else:
        discount = 1 
    #从request处取值
    paymentname = request.POST.get('paymentname',None)
    address_id = request.POST.get('address_id',None)
    cart_ob = Cart.objects.filter(user_id = user_id,selection = '1')
     #计算totalprice和输入时间
    totalprice = 0
    for cart_each in cart_ob:
        try:
            cart_each.goods_id
        except:
            return pack(interface_id,'50112','无效商品')
        if cart_each.goods.remain < cart_each.amount:
            cart_each.amount = cart_each.goods.remain
            return pack(interface_id ,'50111','商品数量不够')
        totalprice = totalprice + cart_each.goods.price * cart_each.amount * discount
    createtime = datetime.datetime.now()
    #创建订单表
    order_row = Order.objects.create(
        user_id = user_id, 
        address_id = address_id,
        totalprice = int(totalprice), 
        discount= discount, 
        createtime = createtime,
        paymentname = paymentname
        )
    #创建订单详情表
    order_detials = []
    for cart_each in cart_ob:
        price=cart_each.goods.price*cart_each.amount*discount
        order_detail_row = OrderDetail.objects.create(order = order_row,goods_id = cart_each.goods.id,price = price)
        order_detials.append(order_detail_row.toDict())
    #创建返回值
    order_resp = order_row.toDict()
    order_resp['order_detail'] = order_detials
    resp = {'data':order_resp}
    return pack(interface_id,data = resp)

@login
@post
def order_finished(request):
    interface_id = '5021'
    #检验订单是否有效
    try:
        order_obj = request.POST.get('order_id',None)
    except:
        return pack(interface_id, '50212','无效订单')
    #检验当前状态是否为‘4’
    if order_obj.status == '4':
        order_obj.status = '5'
        order_obj.save()
    else:
        return pack(interface_id,'50213','订单状态非法')

    return pack(interface_id)
