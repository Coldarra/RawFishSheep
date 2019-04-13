from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime

import sys
sys.path.append('../')


@get
def test(request):
    return HttpResponse('OK')

@get
def undistribution(request):
    interface_id = "6010"
    if request.session["level"] in ["admin", "courier"]:
        try:
            resp = {
                "order": Order.objects.filter(status="1", isdelete="0")
            }
            return pack(interface_id, "0", "成功", resp)
        except:
            return pack(interface_id, "60102", "查询无果")
    else:
        return pack(interface_id, "11", "权限不足")

@post
def distribution(request):
    interface_id = "6011"
    user_id = request.POST.get("user_id", None)
    order_id = request.POST.get("order_id", None)

    try:
        order = Order.objects.get(id=order_id, isdelete="0")
        if not (order.status in ["1", "2"]):
            return pack(interface_id, "60114", "非法操作")
        try:
            user = User.objects.get(id=user_id, isdelete="0", level="courier")
            delivery = Delivery.objects.create(
                order=order,
                user=user,
                receivetime=datetime.datetime.now(),
            )
            delivery.save()
            resp = {
                "delivery": delivery.toDict(),
            }
            return pack(interface_id, "0", "成功", resp)
        except:
            return pack(interface_id, "60112", "无效用户")
    except:
        return pack(interface_id, "60113", "无效订单")

@post
def setting(request):
    interface_id = "6012"
    return HttpResponse("error")

@post
def finish(request):
    interface_id = "6013"
    if request.session["level"] in ["admin", "courier"]:
        order_id = request.POST.get("order_id", None)
        try:
            order = Order.objects.get(id=order_id, isdelete="0")
            delivery_id = order.delivery_by_order.get(id=order_id)
            try:
                delivery = Delivery.objects.get(id=delivery_id, isdelete="0")
                if not order.status == "3":
                    return pack(interface_id, "60134", "订单不在配送中")
                order.status = "4"
                delivery.finishtime = datetime.datetime.now()
                order.save()
                delivery.save()
                return pack(interface_id, "0", "成功")
            except:
                return pack(interface_id, "60133", "无效配送")
        except:
            return pack(interface_id, "60132", "无效订单")
    else:
        return pack(interface_id, "11", "权限不足")