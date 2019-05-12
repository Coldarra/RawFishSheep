import json
import time

from cryptography.fernet import Fernet
from django.http import HttpResponse

cipher_key = b'BxgJ3nXVtc8ErKdoD7gx7R0TkK1x4U8GYMSwcbHH7wE='
cipher = Fernet(cipher_key)


class RFSException(Exception):
    def __init__(self, ret="-1", msg="Exception!"):
        self.ret = ret
        self.msg = msg


class ParamException(RFSException):
    def __init__(self, ret="110", msg="参数非法"):
        self.ret = ret
        self.msg = msg


def service(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        param = {
            "user": getUserInfo(request)
        }
        for k, v in request.GET.items():
            param[k] = v
        for k, v in request.POST.items():
            param[k] = v
        return func(param, * args, **kw)
    return wrapper


def pack(interface_id="null", ret="0", msg="成功", data={}):
    '''interface_id, ret, msg, data'''
    print("\033[1;36m——PACK——\ninterface_id: {}\nret: {}\nmsg: {}\ndata: {}\n\033[0m".format(
        interface_id, ret, msg, data))
    resp = {
        "ret": str(ret),
        "msg": "({}){}".format(interface_id, msg),
        "data": data,
    }
    try:
        return HttpResponse(content=json.dumps(resp), status=200, content_type="application/json")
    except Exception as e:
        print("\033[1;32m数据打包出错\nException: {}\ndata: {}\033[0m".format(e, data))
        resp = {
            "ret": "-1",
            "msg": "数据打包出错(" + str(e) + ")",
            "data": {},
        }
        return HttpResponse(content=json.dumps(resp), status=200, content_type="application/json")


def post(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        if request.method != "POST":
            return pack("method", "100", "接口调用方式错误")
        return func(request, *args, **kw)
    return wrapper


def get(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        print(request)
        if request.method != "GET":
            return pack("method", "100", "接口调用方式错误")
        return func(request, *args, **kw)
    return wrapper


def login(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        # if not request.session.get('isLogin', False):
        #     return pack("login", "10", "未登录")
        token = request.META.get("HTTP_AUTHORIZATION", None)
        token = verifyToken(token)
        if not token:
            return pack("login", "10", "未登录")
        return func(request, *args, **kw)
    return wrapper


def logout(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        request.session.flush()
        request.session['isLogin'] = False
        print("logout")
        return func(request, *args, **kw)
    return wrapper


def admin(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        if not request.session.get('isLogin', False):
            return pack("login", "10", "未登录")
        if not request.session.get('level', 'user') == 'admin':
            return pack("admin", "11", "权限不足")
        return func(request, *args, **kw)
    return wrapper


def courier(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        if not request.session.get('isLogin', False):
            return pack("login", "10", "未登录")
        if not request.session.get('level', 'user') == 'courier':
            return pack("admin", "11", "权限不足")
        return func(request, *args, **kw)
    return wrapper


def general(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        return func(request, *args, **kw)
    return wrapper


def constructToken(userid=None, username=None, level=None):
    token_data = {
        "userid": userid,
        "username": username,
        "level": level,
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    }
    token = 'Bearer ' + str(cipher.encrypt(
        bytes(json.dumps(token_data).encode('utf-8'))), encoding='utf-8')
    # print(verifyToken(token))
    return token


def verifyToken(token):
    print(token)
    try:
        if token[:6] == "Bearer":
            token = token[7:]
        decrypt_data = cipher.decrypt(bytes(token, encoding="utf-8"))
        data = json.loads(decrypt_data)
        return data
    except Exception as e:
        return None


def getUserInfo(request):
    token = request.META.get("HTTP_AUTHORIZATION", None)
    token_data = verifyToken(token)
    if token_data:
        return token_data
    else:
        return {
            "userid": None,
            "username": None,
            "level": None,
            "time": None,
        }
