from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


# 查询当前用户所有的购物车信息


def get_All_Cart(user_id):
    try:
        carts_obj = Cart.objects.filter(user_id=user_id)
    except:
        raise RFSException("40001","获取购物车失败")
    # 生成返回值
    print([cart.toDict() for cart in carts_obj])
    return carts_obj


# cart表中添加商品数据

def append_Cart(goods_id,amount,user_id):
    # 检测参数是否非法
    if amount == None or goods_id == None:
        raise ParamException()
    # 检测商品是否有效
    try:
        goods_obj = Goods.objects.get(id=goods_id)
    except:
        raise RFSException("40012", "无效商品")
    # 检测商品数量是否非法
    if goods_obj.remain < 1:
        raise RFSException("40013", "商品数量非法")
    try:
        if Cart.objects.filter(user_id=user_id, goods_id=goods_id).count() != 0:
            # 获得对象如果对象存在则更新如果不存在报错则跳至except
            cart_obj = Cart.objects.get(user_id=user_id, goods_id=goods_id)
            # 更新对象的amount值
            cart_obj.amount += int(amount)
            cart_obj.save()
        else:
            # 创建新的cart
            cart_obj = Cart.objects.create(
                user_id=user_id, goods_id=goods_id, amount=amount)
        cartreturn = [cart.toDict() for cart in Cart.objects.filter(
            user_id=user_id, selection="1")]
        return cartreturn
    except:
        raise RFSException("40014", "插入失败")


# cart表删除数据
def delete_Cart(user_id,goods_id,cart_id):
    # 检测参数是否非法
    if goods_id == None and cart_id == None:
        raise ParamException()
    # 检测商品是否有效
    try:
        if cart_id:
            cart = Cart.objects.filter(user_id=user_id, id=cart_id).delete()
        if goods_id:
            cart = Cart.objects.filter(
                user_id=user_id, goods_id=goods_id).delete()
    except Exception as e:
        raise RFSException (interface_id, "40022", "无效购物车")

# 直接更改购物车商品数目

def cart_update_amount(user_id,goods_id,amount):
    # 检测参数是否合法
    if goods_id == None or amount == None:
        raise ParamException()
    # 检测参数商品是否有效
    try:
        cart_obj = Cart.objects.get(user_id=user_id, goods_id=goods_id)
    except:
        raise RFSException("40032", "无效商品")
    # 检测商品状态是否合法
    if cart_obj.amount < 0:
        raise RFSException("40033", "状态非法")
    # 修改购物车商品数量
    cart_obj.amount = amount
    cart_obj.save()
    # 生成返回值
    carts = {"cart": cart_obj.toDict()}
    return carts

# 修改购物车商品状态


def cart_update_state(user_id,cart_id,selection):
    # 检测参数是否合法
    if cart_id == None or selection == None:
        raise ParamException()
    # 检测商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
    except: 
        raise RFSException("40032", "无效购物车")
    # 检测商品状态是否合法
    if cart.selection != "0" and cart.selection != "1":
        raise RFSException("40033", "状态非法")
    # 改变商品状态
    try:
        cart.selection = selection
        cart.save()
        # 生成返回值
        cart_update = {"cart": cart.toDict()}
        return cart_update
    except:
        raise RFSException("1", "状态修改失败")

def get_cartlist(user_id):
    cart_obj = Cart.objects.filter(user_id=user_id, selection='1')
    return cart_obj