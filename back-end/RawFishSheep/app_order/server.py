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
def order_all(param):
    interface_id = '5000'
    user_id = param['user']['userid']
    try:
        order_data = get_All(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id, data=order_data)

@login
@service
def order_unfinished(param):
    interface_id = '5001'
    user_id = param['user']['userid']
    try:
        order_data = get_unfinished(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def order_finished(param):
    interface_id = '5002'
    user_id = param['user']['userid']
    try:
        order_data = get_finished(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)


@login
@service
def order_info(param):
    interface_id = '5010'
    user_id = param['user']['userid']
    order_id = param.get('order_id', None)
    try:
        order_data = get_info(user_id,order_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def order_append(param):
    interface_id = '5011'
    user_id = param['user']['userid']
    level = param.get('level', None)
    paymentname = param.get('paymentname', None)
    address_id = param.get('address_id', None)
    try:
        order_data = append_order(user_id,level,paymentname,address_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id, data=order_data)

@login
@service
def order_finished(param):
    interface_id = '5021'
    # 检验订单是否有效
    order_id = param.get('order_id', None)
    try:
        make_finished(order_id)    
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id)
@login
@service
def order_delete(param):
    interface_id = '5031'
    user_id = param['user']['userid']

    try:
        delete_order(user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))    
    return pack(interface_id)
   