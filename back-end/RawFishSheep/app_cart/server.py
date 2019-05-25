from decorator import *
from . import views
from .models import *


def test(param):
    print(param)
    return {
        "ok": ok
    }


@login
@service
def cart_all(param):
    # Auth: ZANGRUIQING
    # Date: 2019.4.12
    interface_id = "4000"
    user_id = param["user"]['userid']
    print(param)
    try:
        cart_obj = views.get_All_Cart(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    # user.login(request)
    resp = {
        "cart": [cart.toDict() for cart in cart_obj]
    }
    return pack(interface_id, data=resp)

@login
@service
def cart_append(param):
    interface_id = "4001"
    goods_id = param.get("goods_id", None)
    amount = param.get("amount", None)
    user_id = param["user"]['userid']
    try:
        cart_data = views.append_Cart(goods_id,amount,user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    resp = {
        "cart": cart_data
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
        views.delete_Cart(user_id,goods_id,cart_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id)


@login
@service
def cart_update_amount(param):
    interface_id = "4003"
    # 从POST中获取数据
    goods_id = param.get("goods_id", None)
    amount = param.get("amount", None)
    user_id = param["user"]['userid']
    try:
        cart_update = views.cart_update_amount(user_id,goods_id,amount)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id, data=cart_update)


@login
@service
def cart_update_state(param):
    interface_id = "4004"
    cart_id = param.get("cart_id", None)
    selection = param.get("selection", None)
    user_id = param["user"]['userid']
    try:
        cart_update = views.cart_update_state(user_id, cart_id,selection)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id=interface_id, data=cart_update)
