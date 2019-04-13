from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

import sys
sys.path.append('../')

# Create your views here.
@get
def test(request):
    return HttpResponse('OK')
#查询当前用户所有的购物车信息
@get
def cart_all(request):
    interface_id = '4000'
    user_id = request.session['userid']
    #从Cart表获取selection=‘1’的商品
    cartinfo = Cart.objects.filter(user_id=user_id, selection='1')
    #生成返回值
    carts = []
    for cart_e in cartinfo:
        carts.append(cart_e.toDict())
    resp = {
        'ret': '0',
        'msg': '成功',
        'data': {'cart': carts}
    }
    return pack(interface_id, data=resp)
#cart表中添加商品数据
@post
def cart_append(request):
    interface_id = '4001'
    #获取request和session的值
    goods_id = request.POST.get('goods_id', None)
    amount_n = request.POST.get('amount', None)
    user_id = request.session['userid']
    #检测参数是否非法
    if amount_n == None or goods_id == None:
        return pack(interface_id, '110', '参数非法')
    #检测商品是否有效
    try:
        n = Goods.objects.get(id=goods_id)
    except:
        return pack(interface_id, '40012', '无效商品')
    #检测商品数量是否非法
    if n.remain < 1:
        return pack(interface_id, '40013', '商品数量非法')
    try:
        try:
            #获得对象如果对象存在则更新如果不存在报错则跳至except
            cart_row = Cart.objects.get(user_id=user_id, goods_id=goods_id)
            new_num = int(amount_n)+cart_row.amount
            #更新对象的amount值
            cart_row.amount = new_num
            cart_row.save()
        except:
            #创建新的数据库row
            cart_row = Cart.objects.create(
                user_id=user_id, goods_id=goods_id, amount=amount_n, selection='1')
        #生成返回值
        resp = cart_row.toDict()
        data_d = {'cart': resp}
        return pack(interface_id, data=data_d)
    except:
        return pack(interface_id, '1', '插入失败')
#cart表删除数据
@post
def cart_delete(request):
    interface_id = '4002'
    #获取request中的数据
    cart_id = request.POST.get('cart_id', None)
    #检测参数是否非法
    if cart_id == None:
        return pack(interface_id, '110', '参数非法')
    user_id = request.session['userid']
    #检测商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
        card = cart.goods.id
    except:
        return pack(interface_id, '40022', '无效商品')
    #检测商品是否非法
    if cart.goods.remain < 1:
        return pack(interface_id, '40013', '商品数量非法')
    try:
        #删除表中数据
        cart.delete()
        return pack(interface_id)
    except:
        return pack(interface_id, "1", "删除失败")
#更新购物车商品树木
@post
def cart_update_amount(request):
    interface_id = '4003'
    #从POST中获取数据
    cart_id = request.POST.get('cart_id', None)
    amount = request.POST.get('amount', None)
    #检测参数是否合法
    if cart_id == None or amount == None:
        return pack(interface_id, '110', '参数非法')
    #检测参数商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
        card = cart.goods.id
    except:
        return pack(interface_id, '40032', '无效商品')
    #检测商品状态是否合法
    if cart.amount < 0:
        return pack(interface_id, '40033', '状态非法')
    #修改购物车商品数量
    try:
        cart.amount = amount
        cart.save()
        #生成返回值
        carts = {'cart': cart.toDict()}
        return pack(interface_id, data=carts)
    except:
        return pack(interface_id, "1", "商品数量修改失败")

#修改购物车商品状态
@post
def cart_update_state(request):
    interface_id = '4004'
    #从POST中获得数据
    cart_id = request.POST.get('cart_id', None)
    selection = request.POST.get('selection', None)
    #检测参数是否合法
    if cart_id == None or selection == None:
        return pack(interface_id, '110', '参数非法')
    user_id = request.session['userid']
    #检测商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return pack(interface_id, '40032', '无效商品')
    #检测商品状态是否合法
    if cart.selection != '0' and cart.selection != '1':
        return pack(interface_id, '40033', '状态非法')
    #改变商品状态
    try:
        cart.selection = selection
        cart.save()
        #生成返回值
        carts = {'cart': cart.toDict()}
        return pack(interface_id, data=carts)
    except:
        return pack(interface_id, "1", "状态修改失败")
