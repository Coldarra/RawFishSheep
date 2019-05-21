from decorator import *
from . import views
from .models import *


def test(param):
    print(param)
    return {
        "ok": ok
    }


@logout
@service
def log_in(param):
    # Auth: ZhengYiming
    # Date: 2019.4.12
    request = None
    interface_id = "1001"
    print("LOGIN...")
    username = param.get('username', None)
    password = param.get('password', None)
    print(param)
    try:
        user = views.getUserByPassword(username, password)
        token = constructToken(user.id, user.username, user.level)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    # user.login(request)
    resp = {
        "user": user.toDict(),
        "token": token,
    }
    return pack(interface_id, data=resp)


@service
def decodeToken(param):
    interface_id = "token"
    token = param.get("token", None)
    token_data = verifyToken(token)
    resp = {
        "user": token_data,
        "token": token
    }
    if token_data:
        return pack(interface_id, data=resp)
    else:
        return pack(interface_id, "token_verify_fail", "无效token, 请重新登录")


@logout
@service
def register(param):
    interface_id = "1000"
    username = param.get('username', None)
    password = param.get('password', None)
    gender = param.get('gender', None)
    phonenumber = param.get('phonenumber', None)
    email = param.get('email', None)

    try:
        user = views.createUser(username, password, gender, phonenumber, email)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {"user": user.toDict()}
    return pack(interface_id=interface_id, data=resp)


@logout
@service
def log_out(param):
    interface_id = "1002"
    return pack(interface_id, "0", "成功", {})


@login
@service
def userinfo(param):
    interface_id = "1003"
    target_user_id = param.get('user_id', None)
    user_id = param["user"]['userid']
    level = param["user"]['level']
    try:
        user = views.getUserByID(target_user_id, user_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {"user": user.toDict()}
    return pack(interface_id=interface_id, data=resp)


@login
@service
def changeinfo(param):
    interface_id = "1004"
    user_id = param["user"]['userid']
    key = param.get('key', None)
    value = param.get('value', None)
    try:
        user = views.changeUserInfo(user_id, key, value)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {"user": user.toDict()}
    return pack(interface_id=interface_id, data=resp)


@login
@service
def delete_account(param):
    interface_id = "1005"
    return pack(interface_id=interface_id)
    # return HttpResponse("error")


@login
@service
def get_address(param):
    interface_id = "1010"
    user_id = param["user"]['userid']
    try:
        user = views.getUserByID(user_id)
        addresses = views.getAddressByUser(user)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    resp = {
        "address": [addr.toDict() for addr in addresses]
    }
    return pack(interface_id, data=resp)


@login
@service
def append_address(param):
    interface_id = "1011"
    user_id = param["user"]['userid']
    name = param.get("name", None)
    phonenumber = param.get("phonenumber", None)
    address = param.get("address", None)
    try:
        # user = views.getUserByID(user_id)
        address = views.createAddress(user_id, name, phonenumber, address)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id, data={"address": addr.toDict()})


@login
@service
def delete_address(param):
    interface_id = "1014"
    user_id = param["user"]['userid']
    address_id = param.get("address_id", None)
    try:
        views.deleteAddress(address_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id)


@login
@service
def default_address(param):
    interface_id = "1013"
    user_id = param["user"]['userid']
    address_id = param.get("address_id", None)
    try:
        address = views.getAddressByID(address_id)
        address = views.setDefaultAddress(address)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+'0', str(e))
    return pack(interface_id, data={"address": addr.toDict()})
