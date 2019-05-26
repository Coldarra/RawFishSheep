from decorator import *
from . import views
from .models import *
from .views import *


def test(param):
    print(param)
    return {
        "ok": ok
    }


@login
@service
def get_all_cart(param):
    # Auth: ZANGRUIQING
    # Date: 2019.5.25
    interface_id = "4000"
    user_id = param["user"]['userid']
    print(param)
    try:
        carts = getAllCart(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    # user.login(request)
    resp = {
        "cart": [cart.toDict() for cart in carts]
    }
    return pack(interface_id, data=resp)


@login
@service
def append_cart(param):
    interface_id = "4001"
    goods_id = param.get("goods_id", None)
    amount = param.get("amount", None)
    user_id = param["user"]['userid']
    try:
        cart = appendToCart(user_id, goods_id, amount)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "cart": cart.toDict()
    }
    return pack(interface_id, data=resp)


@login
@service
def delete_cart(param):
    interface_id = "4002"
    # 获取request中的数据
    cart_id = param.get("cart_id", None)
    goods_id = param.get("goods_id", None)
    user_id = param["user"]['userid']
    try:
        deleteCart(user_id, goods_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id)


@login
@service
def update_amount(param):
    interface_id = "4003"
    # 从POST中获取数据
    goods_id = param.get("goods_id", None)
    amount = param.get("amount", None)
    user_id = param["user"]['userid']
    try:
        cart = updateCartAmount(user_id, goods_id, amount)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "cart": cart.toDict()
    }
    return pack(interface_id, data=resp)


@login
@service
def update_state(param):
    interface_id = "4004"
    cart_id = param.get("cart_id", None)
    selection = param.get("selection", None)
    user_id = param["user"]['userid']
    try:
        cart = updateState(user_id,cart_id, selection)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "cart": cart.toDict()
    }
    return pack(interface_id, data=resp)
