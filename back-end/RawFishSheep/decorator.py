import json

from cryptography.fernet import Fernet
from django.http import HttpResponse

cipher_key = b'BxgJ3nXVtc8ErKdoD7gx7R0TkK1x4U8GYMSwcbHH7wE='
cipher = Fernet(cipher_key)


def pack(interface_id="null", ret="0", msg="成功", data={}):
    '''interface_id, ret, msg, data'''
    resp = {
        "ret": str(ret),
        "msg": "({}){}".format(interface_id, msg),
        "data": data,
    }
    try:
        return HttpResponse(content=json.dumps(resp), status=200, content_type="application/json")
    except Exception as e:
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
        if request.method != "GET":
            return pack("method", "100", "接口调用方式错误")
        return func(request, *args, **kw)
    return wrapper


def login(func):
    def wrapper(request, *args, **kw):
        print('call %s():' % func.__name__)
        # if not request.session.get('isLogin', False):
        #     return pack("login", "10", "未登录")
        token_data = verifyToken(request.META.get("HTTP_AUTHORIZATION", None))
        if not token_data:
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


def verifyToken(encrypt_data):
    try:
        encrypt_data = bytes(encrypt_data, encoding="utf-8")
        decrypt_data = cipher.decrypt(encrypt_data)
        data = json.loads(decrypt_data)
        return data
    except Exception as e:
        return None

