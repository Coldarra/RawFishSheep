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

@get
def cart_all(request):
    interface_id = '4000'
    user_id = request.session['userid']

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
    if Goods.objects.get(id=goods_id).remain<1:
        return pack(interface_id,'40013','商品数量非法')
    #try:
    cart_row = Cart.objects.create(user_id = user_id,goods_id = goods_id, amount=amount_n,selection = '1')
    cars = cart_row.toDict()   
    data_d = {'cart':cars}
    return pack(interface_id,data=data_d)
    #except:
     #   return pack(interface_id,'1','插入失败')

@post
def cart_delete(request):
    interface_id = '4002'
    goods_id = request.POST.get('goods_id',None)
    if goods_id == None:
        return pack(interface_id,'110','参数非法')
    user_id = request.session['userid']
    if Goods.objects.get(id=goods_id):
        pass
    else:
        return pack(interface_id,'40022','无效商品')
    if Goods.objects.get(id=goods_id).remain<1:
        return pack(interface_id,'40013','商品数量非法')
    try:
        Cart.objects.filter(user_id = user_id,goods_id = goods_id).delete()
        return pack(interface_id)
    except:
        return pack(interface_id,"1","删除失败")

@post
def cart_update_state(request):
    interface_id = '4004'
    cart_id = request.POST.get('cart_id',None)
    selection = request.POST.get('selection',None)
    print(cart_id)
    print(selection)
    if cart_id == None or selection == None:
        return pack(interface_id,'110','参数非法')
    user_id = request.session['userid']
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return pack(interface_id,'40032','无效商品')
    if cart.selection != '0' and cart.selection != '1':
        return pack(interface_id,'40033','状态非法')
    #try:
    Cart.objects.filter(id = cart_id).update(selection = selection)
    cartinfo = Cart.objects.filter(id = cart_id)
    carts = []
    for cart_e in cartinfo:
        carts.append(cart_e.toDict())
    return pack(interface_id,data=carts)
 #   except:
  #      return pack(interface_id,"1","状态修改失败")



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