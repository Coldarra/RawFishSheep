import datetime
import random
import re
import time

from decorator import *
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# @get
def test(interface_id, ok):
    print(ok)
    return {
        "ok": ok
    }


regular_list = {
    "username": "^[\u4e00-\u9fa5_a-zA-Z0-9_]{3,15}$",
    "password": "^[A-Za-z0-9]{6,16}$",
    "phonenumber": "^1[0-9]{10}$",
    "email": "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
}


def decodeToken(request):
    interface_id = "token"
    token = request.META.get("HTTP_AUTHORIZATION", None)
    token_data = verifyToken(token)
    if token_data:
        return pack(interface_id, data={"user": token_data, "token": token})
    else:
        return pack(interface_id, "token_verify_fail", "无效token, 请重新登录")


@logout
@post
def register(request):
    interface_id = "1000"
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    gender = request.POST.get('gender', None)
    phonenumber = request.POST.get('phonenumber', None)
    email = request.POST.get('email', None)
    registertime = datetime.datetime.now()

    try:
        user = User.objects.get(username=username)
        return pack(interface_id, "10001", "用户名重复")
    except:
        if not re.match(regular_list["username"], username, flags=0):
            return pack(interface_id, "10002", "用户名非法")

    try:
        user = User.objects.get(phonenumber=phonenumber)
        return pack(interface_id, "10004", "手机号重复")
    except:
        if not re.match(regular_list["phonenumber"], phonenumber, flags=0):
            return pack(interface_id, "10005", "手机号非法")

    try:
        user = User.objects.create(
            username=username,
            password=make_password(password),
            gender=gender,
            phonenumber=phonenumber,
            email=email,
            registertime=registertime,
        )
        resp = {
            "user": {
                "userid": user.id,
                "username": user.username,
                "level": user.level,
            }
        }
        return pack(interface_id=interface_id, data=resp)

    except Exception as e:
        print(e)
        return pack(interface_id, "null", "用户创建失败，原因未知", resp)


@logout
@post
def log_in(request):
    # Auth: ZhengYiming
    # Date: 2019.4.12
    interface_id = "1001"
    print("LOGIN...")
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    # print(request.POST)
    if username == None or password == None:
        return pack(interface_id, "110", "参数非法")

    user = None
    try:  # 姓名登陆
        user = User.objects.get(username=username)
    except:
        pass
    try:  # 手机号登陆
        user = User.objects.get(phonenumber=username)
    except:
        pass
    try:  # 邮箱登陆
        user = User.objects.get(email=username)
    except:
        pass
    if user:  # 存在用户
        token_data = {
            "userid": user.id,
            "username": user.username,
            "level": user.level,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        token = 'Bearer ' + str(cipher.encrypt(
            bytes(json.dumps(token_data).encode('utf-8'))), encoding='utf-8')
        print(user)
        print(verifyToken(token))
        if check_password(password, user.password):
            print("验证成功")  # 比较成功，跳转index
            user.login(request)
            resp = {
                "user": {
                    "userid": user.id,
                    "username": user.username,
                    "level": user.level,
                },
                "token": token,
            }
            return pack(interface_id, data=resp)
        else:
            return pack(interface_id, "10012", "密码错误")
    else:
        return pack(interface_id, "10011", "用户名不存在")

    return pack(interface_id, "10013", "登录受限")


@post
def checklogin(request):
    interface_id = "checklogin"
    if not request.session.get("isLogin", False):
        return pack(interface_id, data={"isLogin": False})
    user_id = request.session["userid"]
    user = User.objects.get(id=user_id)
    return pack(interface_id, data={"isLogin": True, "user": user.toDict()})


@logout
def log_out(request):
    interface_id = "1002"
    return pack(interface_id, "0", "成功", {})


@login
@post
def userinfo(request):
    interface_id = "1003"
    user_id = request.POST.get('user_id', None)
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except:
            return pack(interface_id, "10032", "查无此人")
        if user.level != "courier":
            return pack(interface_id, "10031", "权限不足")
    else:
        user_id = request.session["userid"]
        user = User.objects.get(id=user_id)
        return pack(interface_id, data={"user": user.toDict()})


@login
@post
def changeinfo(request):
    interface_id = "1004"
    user_id = request.session["userid"]
    key = request.POST.get('key', None)
    value = request.POST.get('value', None)

    if key == None or value == None:
        return pack(interface_id, "110", "参数非法")

    if key not in ["username", "password", "phonenumber", "email", "about"]:
        return pack(interface_id, "10042", "未知属性")

    if key in ["username", "password", "phonenumber", "email"]:
        if not re.match(regular_list[key], value, flags=0):
            return pack(interface_id, "110", "参数格式错误")

    user = User.objects.get(id=user_id)
    if key == "username":
        user.username = value
    elif key == "password":
        user.password = make_password(value)
    elif key == "phonenumber":
        user.phonenumber = value
    elif key == "email":
        user.email = value
    elif key == "about":
        user.about = value
    user.save()
    user.login(request)
    return pack(interface_id)


@login
@post
def delete_account(request):
    interface_id = "1005"
    return HttpResponse("error")


@login
@get
def get_address(request):
    interface_id = "1010"
    user_id = request.session["userid"]
    resp = {
        "address": [addr.toDict() for addr in Address.objects.filter(user_id=user_id, status="d")]
    }
    return pack(interface_id, data=resp)


@login
@post
def append_address(request):
    interface_id = "1011"
    user_id = request.session["userid"]
    name = request.POST.get("name", None)
    phonenumber = request.POST.get("phonenumber", None)
    address = request.POST.get("address", None)
    if None in [name, phonenumber, address]:
        return pack(interface_id, "110", "参数非法")
    addr = Address.objects.create(
        user_id=user_id,
        name=name,
        phonenumber=phonenumber,
        address=address,
    )
    if Address.objects.filter(user_id=user_id).count() == 1:
        addr.update(status='0')

    return pack(interface_id, data={"address": addr.toDict()})


@login
@post
def default_address(request):
    interface_id = "1013"
    user_id = request.session["userid"]
    address_id = request.POST.get("address_id", None)
    if not address_id:
        return pack(interface_id, "10132", "地址不存在")

    Address.objects.filter(status='0').update(status='1')
    try:
        addr = Address.objects.get(id=address_id)
        addr.status = '0'
        addr.save()
    except Exception as e:
        return pack(interface_id, "10132", "地址不存在")
    return pack(interface_id, data={"address": addr.toDict()})


@login
@post
def delete_address(request):
    interface_id = "1014"
    user_id = request.session["userid"]
    address_id = request.POST.get("address_id", None)
    if not address_id:
        return pack(interface_id, "10132", "地址不存在")

    try:
        addr = Address.objects.get(id=address_id)
        addr.toDelete()
    except Exception as e:
        return pack(interface_id, "10132", "地址不存在")
    return pack(interface_id)
