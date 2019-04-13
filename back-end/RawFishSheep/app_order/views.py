from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

import sys
sys.path.append('../')
from decorator import *

from .models import *
# Create your views here.
@get
def test(request):
    return HttpResponse('OK')
#查询当前用户所有的购物车信息

@get
def order_all(request):
    interface_id = '5000'
    user_id = request.session['userid']

    try:
        order = Order.objects.filter(user_id = user_id)
    except:
        pass
    orders = []
    for ord in order:
        orders.append(ord.toDict())
    resp = {
        'ret':'0',
        'msg':"成功",
        'data':orders
    }
    return pack(interface_id,data = resp)
   

@get
def order_unfinished(request):
    interface_id = '5001'
    user_id = request.session['userid']

    try:
        order = Order.objects.filter(user_id)
    except:
        pass