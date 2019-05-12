import datetime
import random
import re
import time

from decorator import *
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from . import views


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
        user = views.getUser(username, password)
        token = constructToken(user.id, user.username, user.level)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        print("\033[1;36m{}\033[0m".format(e))
        return pack(interface_id, interface_id+'0', str(e))
    # user.login(request)
    resp = {
        "user": user.toDict(),
        "token": token,
    }
    return pack(interface_id, data=resp)
