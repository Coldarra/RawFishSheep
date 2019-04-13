from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

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
def cart_all(request):
    interface_id = '4000'
    user_id = request.session['userid']
    #从Cart表获取selection=‘1’的
    cartinfo = Cart.objects.filter(user_id = user_id,selection = '1')
    carts = []
    for cart_e in cartinfo:
        carts.append(cart_e.toDict())
    resp = {
        'ret':'0',
        'msg':'成功',
        'data':{'cart':carts}
    }
    return pack(interface_id,data=resp)

@post
def cart_append(request):
    interface_id = '4001'
    goods_id = request.POST.get('goods_id',None)
    amount_n = request.POST.get('amount',None)
    user_id = request.session['userid']
    if amount_n==None or goods_id==None:
        return pack(interface_id,'110','参数非法')
    try:
        n = Goods.objects.get(id=goods_id) 
    except:
        return pack(interface_id,'40012','无效商品')
    if n.remain<1:
        return pack(interface_id,'40013','商品数量非法')
    try:
        try:
            cart_row = Cart.objects.get(user_id = user_id, goods_id = goods_id)
            new_num = int(amount_n)+cart_row.amount
            cart_row.amount = new_num
            cart_row.save()
        except:
            cart_row = Cart.objects.create(user_id = user_id,goods_id = goods_id, amount=amount_n,selection = '1')    
        resp = cart_row.toDict()   
        data_d = {'cart':resp}
        return pack(interface_id,data=data_d)
    except:
        return pack(interface_id,'1','插入失败')

@post
def cart_delete(request):
    interface_id = '4002'
    cart_id = request.POST.get('cart_id',None)
    if cart_id == None:
        return pack(interface_id,'110','参数非法')
    user_id = request.session['userid']
    try:
        cart = Cart.objects.get(id=cart_id)
        card = cart.goods.id
    except:
        return pack(interface_id,'40022','无效商品')
    if cart.goods.remain<1:
        return pack(interface_id,'40013','商品数量非法')
    try:
        cart.delete()
        return pack(interface_id)
    except:
        return pack(interface_id,"1","删除失败")

@post
def cart_update_amount(request):
    interface_id = '4003'
    cart_id = request.POST.get('cart_id',None)
    amount = request.POST.get('amount',None)
    if cart_id == None or amount == None:
        return pack(interface_id,'110','参数非法')
    try:
        cart = Cart.objects.get(id=cart_id)
        card = cart.goods.id
    except:
        return pack(interface_id,'40032','无效商品')
    if cart.amount < 0:
        return pack(interface_id,'40033','状态非法')
    try:
        cart.amount = amount
        cart.save()
        carts = {'cart':cart.toDict()}
        return pack(interface_id,data=carts)
    except:
        return pack(interface_id,"1","商品数量修改失败")


@post
def cart_update_state(request):
    interface_id = '4004'
    cart_id = request.POST.get('cart_id',None)
    selection = request.POST.get('selection',None)
    if cart_id == None or selection == None:
        return pack(interface_id,'110','参数非法')
    user_id = request.session['userid']
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return pack(interface_id,'40032','无效商品')
    if cart.selection != '0' and cart.selection != '1':
        return pack(interface_id,'40033','状态非法')
    try:
        cart.selection = selection
        cart.save()
        carts = {'cart':cart.toDict()}
        return pack(interface_id,data=carts)
    except:
        return pack(interface_id,"1","状态修改失败")



@get
def order_all(request):
    interface_id = '5000'
    user_id = request.session['userid']

    try:
        order = Order.objects.filter(user_id = user_id)
    except:
        pass
    orders = []
    for ord in order:
        orders.append(ord.toDict())
    resp = {
        'ret':'0',
        'msg':"成功",
        'data':orders
    }
    return pack(interface_id,data = resp)
   

@get
def order_unfinished(request):
    interface_id = '5001'
    user_id = request.session['userid']

    try:
        order = Order.objects.filter(user_id)
    except:
        pass