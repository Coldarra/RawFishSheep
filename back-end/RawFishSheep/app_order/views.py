from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import datetime
import sys
sys.path.append('../')
from decorator import *

from .models import *
# Create your views here.
@get
def test(request):
    return HttpResponse('OK')
#查询当前用户所有的购物车信息

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
   

@get
def order_unfinished(request):
    interface_id = '5001'
    user_id = request.session['userid']

    try:
        order = Order.objects.filter(user_id)
    except:
        pass
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
    paymentname = request.POST.get('paymentname',None)
    address_id = request.POST.get('address_id',None)
    cart_ob = Cart.objects.filter(user_id = user_id,selection = '1')
     #创建订单表
    totalprice = 0
    for cart_each in cart_ob:
        totalprice = totalprice + cart_each.goods.price * cart_each.amount * discount
    createtime = datetime.datetime.now()
    
    order_row = Order.objects.create(user_id = user_id, address_id = address_id,
    totalprice = totalprice, discount= discount, createtime = createtime,finishtime = None,paymentname = paymentname)

    order_detials = []
    for cart_each in cart_ob:
        try:
            price=cart_each.goods.price*cart_each.amount*discount
            order_detail_row = OrderDetail.objects.create(order_id = order_row.id,goods_id = cart_each.goods.id,price = price)
            order_detials.append(order_detail_row.toDict())
        except:
            return pack(interface_id,'1','订单详情表插入失败')
    return pack(interface_id)

    


        