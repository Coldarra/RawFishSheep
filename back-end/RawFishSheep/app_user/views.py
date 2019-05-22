import datetime
import random
import re
import time

from decorator import *
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


regular_list = {
    "username": "^[\u4e00-\u9fa5_a-zA-Z0-9_]{3,15}$",
    "password": "^[A-Za-z0-9]{6,16}$",
    "phonenumber": "^1[0-9]{10}$",
    "email": "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
}


def getUserByID(target_user_id=None, user_id=None):  # target_user_id: 被查  user_id: 查
    if target_user_id == None:
        raise ParamException()
    if User.objects.filter(id=target_user_id).count():
        target_user = User.objects.get(id=target_user_id)
    else:
        raise RFSException("10032", "查无此人")
    # TODO: 权限管理
    # if user_id != None:
    #     user = User.objects.get(id=user_id)
    return target_user


def getUserByPassword(username=None, password=None):
    if username == None or password == None:
        raise ParamException()
    user = None
    if User.objects.filter(username=username).count():
        user = User.objects.get(username=username)
    elif User.objects.filter(phonenumber=username).count():
        user = User.objects.get(phonenumber=username)
    elif User.objects.filter(email=username).count():
        user = User.objects.get(email=username)
    else:
        raise RFSException("10011", "用户名不存在")
    if check_password(password, user.password):
        print("验证成功")
        return user
    else:
        raise RFSException("10012", "密码错误")
    # TODO
    raise RFSException("10013", "登录受限")


def createUser(username=None, password=None, gender=None, phonenumber=None, email=None):
    if User.objects.filter(username=username).count():
        user = User.objects.get(username=username)
        raise RFSException("10001", "用户名重复")
    else:
        if not re.match(regular_list["username"], username, flags=0):
            raise RFSException("10002", "用户名非法")
    if User.objects.filter(phonenumber=phonenumber).count():
        user = User.objects.get(phonenumber=phonenumber)
        raise RFSException("10004", "手机号重复")
    else:
        if not re.match(regular_list["phonenumber"], phonenumber, flags=0):
            raise RFSException("10005", "手机号非法")
    user = User.objects.create(
        username=username,
        password=make_password(password),
        gender=gender,
        phonenumber=phonenumber,
        email=email,
        # registertime=datetime.datetime.now(),
    )
    return user


def changeUserInfo(user_id, key, value):
    user = getUserByID(user_id)
    if key == None or value == None:
        raise ParamException()
    if key not in ["username", "password", "phonenumber", "email", "about"]:
        raise RFSException("10042", "未知属性")
    if key in ["username", "password", "phonenumber", "email"]:
        if not re.match(regular_list[key], value, flags=0):
            raise RFSException("10043", "参数"+key+"格式错误")
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
    # user.login(request)
    return user


def getAddressByUser(user):
    addresses = user.address_by_user.exclude(status="d")
    return addresses


def getAddressByID(address_id=None):
    if address_id == None:
        raise ParamException()
    if Address.objects.filter(id=address_id).count():
        address = Address.objects.get(id=address_id)
    else:
        raise RFSException("10103", "地址信息查询无果")
    return address


def createAddress(user_id=None, name=None, phonenumber=None, address=None, detail=None):
    if None in [user_id, phonenumber, address, None]:
        raise ParamException()
    address = Address.objects.create(
        user_id=user_id,
        name=name,
        phonenumber=phonenumber,
        address=address,
        detail=detail,
    )
    if Address.objects.filter(user_id=user_id).count() == 1:
        address.status = '0'
        address.save()
    return address


def deleteAddress(address_id):
    address = getAddressByID(address_id)
    address.toDelete()


def setDefaultAddress(address):
    if not address:
        raise RFSException("10132", "地址不存在")
    user_id = address.user_id
    Address.objects.filter(user_id=user_id, status='0').update(status='1')
    address.update(status='0')
    return address
