from .models import *
from decorator import *

from app_goods.views import getGoodsByID

# 查询当前用户所有的购物车信息


def getCartByUser(user_id=None):
    if user_id == None:
        raise ParamException()
    return Cart.objects.filter(user_id=user_id)


def getSelectedCart(user_id=None):
    if user_id == None:
        raise ParamException()
    return Cart.objects.filter(user_id=user_id, selection="1")


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


def deleteCartByGoods(user_id=None, goods_id=None):
    if None in [user_id, goods_id]:
        raise ParamException()
    Cart.objects.filter(user_id=user_id,
                        goods_id=goods_id).delete()


def deleteCartByUser(user_id=None):
    if None in [user_id, goods_id]:
        raise ParamException()
    Cart.objects.filter(user_id=user_id).delete()


def deleteSelectedCart(user_id=None):
    if user_id == None:
        raise ParamException()
    Cart.objects.filter(user_id=user_id, selection="1").delete()


def setCartAmount(user_id=None, goods_id=None, amount=None):
    if None in [user_id, goods_id, amount]:
        raise ParamException()
    amount = int(amount)
    cart = getCartByGoods(user_id, goods_id)
    if amount <= 0:
        raise RFSException("40033", "购物车商品数量非法")
    cart.amount = amount
    cart.save()
    return cart


def setCartSelection(user_id=None, goods_id=None, selection=None):
    # 检测参数是否合法
    if None in [user_id, goods_id, selection]:
        raise ParamException()
    cart = getCartByGoods(user_id, goods_id)
    # 检测商品状态是否合法
    if cart.selection != "0" and cart.selection != "1":
        raise RFSException("40033", "状态非法")
    # 改变商品状态
    cart.selection = selection
    cart.save()
    return cart
