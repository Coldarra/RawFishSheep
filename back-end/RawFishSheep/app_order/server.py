from decorator import *
from . import views
from .views import *


def get_order(param, mode):
    interface_id = '5000'
    user_id = param['user']['userid']
    try:
        orders = getOrderByUser(user_id, mode)
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
def get_all_order(param):
    return get_order(param, 'all')


@login
@service
def get_unfinished_order(param):
    return get_order(param, 'unfinished')


@login
@service
def get_finished_order(param):
    return get_order(param, 'finished')


@login
@service
def get_order_info(param):
    interface_id = '5010'
    user_id = param['user']['userid']
    order_id = param.get('order_id', None)
    try:
        order = getOrderByID(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "order": order.toDict()
    }
    return pack(interface_id, data=resp)


@login
@service
def append_order(param):
    interface_id = '5011'
    user_id = param['user']['userid']
    level = param['user']['level']
    paymentname = param.get('paymentname', None)
    address_id = param.get('address_id', None)
    discount = 0.9 if level == "vip" else 1
    try:
        order = createOrder(user_id, discount, paymentname, address_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "order": order
    }
    return pack(interface_id, data=resp)


@login
@service
def confirm_order(param):
    interface_id = '5021'
    order_id = param.get('order_id', None)
    try:
        confirmOrder(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id)


@login
@service
def delete_order(param):
    interface_id = '5031'
    user_id = param['user']['userid']
    order_id = param.get('order_id', None)
    try:
        deleteOrder(order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id)
