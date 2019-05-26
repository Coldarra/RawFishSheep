from .models import *
from decorator import *

from app_goods.views import getGoodsByID

# 查询当前用户所有的购物车信息


def getAllCart(user_id=None):
    if user_id == None:
        raise ParamException()
    return Cart.objects.filter(user_id=user_id)


def getCartByGoods(user_id=None, goods_id=None):
    if None in [user_id, goods_id]:
        raise ParamException()
    if Cart.objects.filter(user_id=user_id, goods_id=goods_id).count() <= 0:
        raise RFSException("40012", "无效购物车商品")
    return Cart.objects.get(user_id=user_id, goods_id=goods_id)


def checkCartByGoods(user_id, goods_id):
    return Cart.objects.filter(user_id=user_id, goods_id=goods_id).count() > 0


def createCart(user_id=None, goods_id=None, amount=None):
    if None in [user_id, goods_id, amount]:
        raise ParamException()
    if checkCartByGoods(user_id, goods_id):
        appendToCart(user_id, goods_id, amount)
    return Cart.objects.create(
        user_id=user_id, goods_id=goods_id, amount=amount)


def appendToCart(user_id=None, goods_id=None, amount=None):
    if None in [user_id, goods_id, amount]:
        raise ParamException()
    amount = int(amount)
    if getGoodsByID(goods_id).remain < amount:
        raise RFSException("40013", "商品余辆不足")
    if checkCartByGoods(user_id, goods_id):
        cart_obj = getCartByGoods(user_id, goods_id)
        cart_obj.amount += amount
        cart_obj.save()
        return cart_obj
    else:
        return createCart(user_id, goods_id, amount)


def deleteCart(user_id=None, goods_id=None):
    if None in [user_id, goods_id]:
        raise ParamException()
    cart = Cart.objects.filter(user_id=user_id,
                               goods_id=goods_id).delete()


def updateCartAmount(user_id=None, goods_id=None, amount=None):
    if None in [user_id, goods_id, amount]:
        raise ParamException()
    amount = int(amount)
    cart = getCartByGoods(user_id, goods_id)
    if amount <= 0:
        raise RFSException("40033", "购物车商品数量非法")
    cart.amount = amount
    cart.save()
    return cart

# 修改购物车商品状态


def updateState(cart_id, selection):
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
