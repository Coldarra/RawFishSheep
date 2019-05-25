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
def get_all_order(param):
    interface_id = '5000'
    user_id = param['user']['userid']
    try:
        order_data = getAll(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id, data=order_data)

@login
@service
def get_unfinished_order(param):
    interface_id = '5001'
    user_id = param['user']['userid']
    try:
        order_data = getUnfinished(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def get_finished_order(param):
    interface_id = '5002'
    user_id = param['user']['userid']
    try:
        order_data = getFinished(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)


@login
@service
def get_order_info(param):
    interface_id = '5010'
    user_id = param['user']['userid']
    order_id = param.get('order_id', None)
    try:
        order_data = getInfo(user_id,order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def append_order(param):
    interface_id = '5011'
    user_id = param['user']['userid']
    level = param.get('level', None)
    paymentname = param.get('paymentname', None)
    address_id = param.get('address_id', None)
    try:
        order_data = appendOrder(user_id,level,paymentname,address_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def make_order_finished(param):
    interface_id = '5021'
    # 检验订单是否有效
    order_id = param.get('order_id', None)
    try:
        makeFinished(order_id)    
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

    try:
        deleteOrder(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id)
   