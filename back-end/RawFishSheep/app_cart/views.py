from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


# 查询当前用户所有的购物车信息

@login
@service
def cart_all(param):
    interface_id = "4000"
    user_id = param["user"].get("userid", None)
    # 从Cart表获取selection="1"的商品
    carts = Cart.objects.filter(user_id=user_id, selection="1")
    # 生成返回值
    resp = {
        "cart": [cart.toDict() for cart in carts]
    }
    return pack(interface_id, data=resp)


# cart表中添加商品数据

@login
@service
def cart_append(param):
    interface_id = "4001"
    # 获取request和session的值
    goods_id = param.get("goods_id", None)
    amount = param.get("amount", None)
    user_id = param["user"].get("userid", None)
    # 检测参数是否非法
    if amount == None or goods_id == None:
        return pack(interface_id, "110", "参数非法")
    # 检测商品是否有效
    try:
        goods = Goods.objects.get(id=goods_id)
    except:
        return pack(interface_id, "40012", "无效商品")
    # 检测商品数量是否非法
    if goods.remain < 1:
        return pack(interface_id, "40013", "商品数量非法")
    try:
        if Cart.objects.filter(user_id=user_id, goods_id=goods_id).count() != 0:
            # 获得对象如果对象存在则更新如果不存在报错则跳至except
            cart = Cart.objects.get(user_id=user_id, goods_id=goods_id)
            # 更新对象的amount值
            cart.amount += int(amount)
            cart.save()
        else:
            # 创建新的cart
            cart_new = Cart.objects.create(
                user_id=user_id, goods_id=goods_id, amount=amount)
        resp = {"cart": [cart.toDict() for cart in Cart.objects.filter(
            user_id=user_id, selection="1")]}
        print(resp)
        return pack(interface_id, data=resp)
    except Exception as e:
        print(e)
        return pack(interface_id, "1", "插入失败")


# cart表删除数据
@login
@post
def cart_delete(request):
    interface_id = "4002"
    # 获取request中的数据
    cart_id = request.POST.get("cart_id", None)
    goods_id = request.POST.get("goods_id", None)
    # 检测参数是否非法
    if cart_id == None and goods_id == None:
        return pack(interface_id, "110", "参数非法")
    user_id = request.session["userid"]
    # 检测商品是否有效
    try:
        if cart_id:
            cart = Cart.objects.filter(id=cart_id).delete()
        if goods_id:
            cart = Cart.objects.filter(goods_id=goods_id).delete()
    except Exception as e:
        print(e)
        return pack(interface_id, "40022", "无效商品")
    # cart.toDelete()
    return pack(interface_id)


# 直接更改购物车商品数目
@login
@post
def cart_update_amount(request):
    interface_id = "4003"
    # 从POST中获取数据
    cart_id = request.POST.get("cart_id", None)
    amount = request.POST.get("amount", None)
    # 检测参数是否合法
    if cart_id == None or amount == None:
        return pack(interface_id, "110", "参数非法")
    # 检测参数商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return pack(interface_id, "40032", "无效商品")
    # 检测商品状态是否合法
    if cart.amount < 0:
        return pack(interface_id, "40033", "状态非法")
    # 修改购物车商品数量

    cart.amount = amount
    cart.save()
    # 生成返回值
    carts = {"cart": cart.toDict()}
    return pack(interface_id, data=carts)

# 修改购物车商品状态


@login
@post
def cart_update_state(request):
    interface_id = "4004"
    # 从POST中获得数据
    cart_id = request.POST.get("cart_id", None)
    selection = request.POST.get("selection", None)
    # 检测参数是否合法
    if cart_id == None or selection == None:
        return pack(interface_id, "110", "参数非法")
    user_id = request.session["userid"]
    # 检测商品是否有效
    try:
        cart = Cart.objects.get(id=cart_id)
    except:
        return pack(interface_id, "40032", "无效商品")
    # 检测商品状态是否合法
    if cart.selection != "0" and cart.selection != "1":
        return pack(interface_id, "40033", "状态非法")
    # 改变商品状态
    try:
        cart.selection = selection
        cart.save()
        # 生成返回值
        carts = {"cart": cart.toDict()}
        return pack(interface_id, data=carts)
    except:
        return pack(interface_id, "1", "状态修改失败")
