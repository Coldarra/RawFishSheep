from .models import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime


from decorator import *


@get
def test(request):
    return HttpResponse('OK')

@login
@get
def undistribution(request): #获取未分配订单
    interface_id = "6010"
    if request.session["level"] in ["admin", "courier"]:
        try:
            resp = {
                "order": [],
            }
            for order in Order.objects.filter(status="1", isdelete="0"):
                resp["order"].append(order.toDict())
            return pack(interface_id, "0", "成功", resp)
        except:
            return pack(interface_id, "60102", "查询无果")
    else:
        return pack(interface_id, "11", "权限不足")

@login
@post
def distribution(request): #分配配送员接单
    interface_id = "6011"
    user_id = request.POST.get("user_id", None)
    order_id = request.POST.get("order_id", None)

    if request.session["level"] in ["admin", "courier"]:
        try:
            order = Order.objects.get(id=order_id, isdelete="0")
            if not order.status == "1":
                return pack(interface_id, "60114", "非法操作")
            try:
                user = User.objects.get(id=user_id, isdelete="0", level="courier")
                delivery = Delivery.objects.create(
                    order=order,
                    user=user,
                    createtime=datetime.datetime.now(),
                )
                order.status = "2"
                order.save()    
                resp = {
                    "delivery": delivery.toDict(),
                    "order": order.toDict,
                }
                return pack(interface_id, "0", "成功", resp)
            except Exception as e:
                print(e)
                return pack(interface_id, "60112", "无效用户")
        except:
            return pack(interface_id, "60113", "无效订单")
    else:
        return pack(interface_id, "11", "权限不足")
    

@login
@post
def setting(request):#修改配送信息，暂无法修改
    interface_id = "6012"
    return HttpResponse("error")


@login
@post
def finish(request):#配送完成，配送员的确认
    interface_id = "6013"
    if request.session["level"] in ["admin", "courier"]:
        order_id = request.POST.get("order_id", None)
        try:
            order = Order.objects.get(id=order_id, isdelete="0")
            try:
                delivery = Delivery.objects.get(order_id=order_id, isdelete="0")
                if not order.status == "3":
                    return pack(interface_id, "60134", "非法操作")
                order.status = "4"
                delivery.finishtime = datetime.datetime.now()
                order.save()
                delivery.save()
                resp = {
                    "delivery": delivery.toDict(),
                    "order": order.toDict(),
                }
                return pack(interface_id, "0", "成功", resp)
            except:
                return pack(interface_id, "60133", "无效配送")
        except:
            return pack(interface_id, "60132", "无效订单")
    else:
        return pack(interface_id, "11", "权限不足")


@login
@post
def receive(request):#配送员确认收货
    interface_id = "6014"
    if request.session["level"] in ["admin", "courier"]:
        order_id = request.POST.get("order_id", None)
        try:
            order = Order.objects.get(id=order_id, isdelete="0")
            try:
                delivery = Delivery.objects.get(order_id=order_id, isdelete="0")
                if not order.status == "2":
                    return pack(interface_id, "60143", "非法操作")
                order.status = "3"
                delivery.receivetime = datetime.datetime.now()
                order.save()
                delivery.save()
                resp = {
                    "delivery": delivery.toDict(),
                    "order": order.toDict(),
                }
                return pack(interface_id, "0", "成功", resp)
            except Exception as e:
                print(e)
                return pack(interface_id, "60142", "无效配送")
        except Exception as e1:
            print(e1)
            return pack(interface_id, "60141", "无效订单")
    else:
        return pack(interface_id, "11", "权限不足")

@admin
@post
def audit(request):#管理员审核订单（QAQ结果郑懿鸣说默认审核好了）
    interface_id = "6015"
    order_id = request.POST.get("order_id", None)
    try:
        order = Order.objects.get(id=order_id, isdelete="0")
        try:
            delivery = Delivery.objects.get(order_id=order_id, isdelete="0")
            if not order.status == "0":
                return pack(interface_id, "60153", "非法操作")
            order.status = "1"
            order.save()
            resp = {
                "delivery": delivery.toDict(),
                "order": order.toDict(),
            }
            return pack(interface_id, "0", "成功", resp)
        except:
            return pack(interface_id, "60152", "无效配送")
    except:
        return pack(interface_id, "60151", "无效订单")
