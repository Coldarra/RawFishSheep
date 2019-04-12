from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import *
import datetime
import random
import re

import sys
sys.path.append('../')
from decorator import *


@get
def test(request):
    return HttpResponse('OK')


regular_list = {
    "username": "^[\u4e00-\u9fa5_a-zA-Z0-9_]{3,15}$",
    "password": "^[A-Za-z0-9]{6,16}$",
    "phonenumber": "^1[0-9]{10}$",
    "email": "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
}


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
            "userid": user.id,
            "username": user.username,
            "level": user.level,
        }
        return pack(interface_id=interface_id, data=resp)

    except Exception as e:
        print(e)
        return pack(interface_id, "null", "用户创建失败，原因未知", resp)


@logout
@post
def log_in(request):
    interface_id = "1001"
    print("LOGIN...")
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
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
        print(user)
        if check_password(password, user.password):
            print("验证成功")  # 比较成功，跳转index
            user.login(request)
            resp = {
                "userid": user.id,
                "username": user.username,
                "level": user.level,
            }
            return pack(interface_id, data=resp)
        else:
            return pack(interface_id, "10012", "密码错误")
    else:
        return pack(interface_id, "10011", "用户名不存在")

    return pack(interface_id, "10013", "登录受限")


@logout
def log_out(request):
    interface_id = "1002"
    return pack(interface_id, "0", "成功", resp)
