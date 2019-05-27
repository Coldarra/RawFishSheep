from decorator import *
from .views import *
from app_order.views import *


@login
@service
def get_undistribution(param): #获取未分配订单
    interface_id = "6010"
    try:
        orders = getOrderByMode("preparing")
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "order": [order.toDict() for order in orders]
    }
    return pack(interface_id, data=resp)


@login
@service
def audit_order(param):#processing to examining
    interface_id = "6015"
    order_id = param.get("order_id", None)

    try:
        changeDelivery(order_id=order_id, mode="processing")
        order = getOrderByID(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "order": order.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def distribut_order(param): #examining to preparing
    interface_id = "6011"
    order_id = param.get("order_id", None)

    try:
        changeDelivery(order_id=order_id, mode="examining")
        order = getOrderByID(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "order": order.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def receive_order(param):#配送员确认收货 preparing to delivering
    interface_id = "6014"
    user_id = param.get("user_id", None)
    order_id = param.get("order_id", None)
    try:
        changeDelivery(user_id, order_id, mode="preparing")
        order = getOrderByID(order_id)
        delivery = getDeliverByOrder(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "delivery": delivery.toDict(),
        "order": order.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def finish_order(param):#配送完成，配送员的确认 delivering to delivered
    interface_id = "6013"
    order_id = param.get("order_id", None)
    try:
        changeDelivery(order_id=order_id, mode="delivering")
        order = getOrderByID(order_id)
        delivery = getDeliverByOrder(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "delivery": delivery.toDict(),
        "order": order.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@post
def setting(param):#修改配送信息，暂无法修改
    interface_id = "6012"
    return HttpResponse("error")