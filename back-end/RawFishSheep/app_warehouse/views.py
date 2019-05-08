from django.shortcuts import render
from decorator import *
from django.http import HttpResponse
import datetime
import pytz
import time
from .models import *

# Create your views here.

@get
def test(request):
    return HttpResponse('OK')

@admin
@get
def get_warehouseinfo(request):
    interface_id = "3000"
    resp = {
        "warehouse":[tmpware.toDict() for tmpware in Warehouse.objects.all()]
    }
    return pack(interface_id,data = resp)

@admin
@post
def append_warehouse(request):
    interface_id = "3001"
    address = request.POST.get("address",None)
    warehouse_id= request.POST.get("warehouse_id",None)
    if not address:
        return pack(interface_id,"110","参数非法")
    if Warehouse.objects.filter(address = address).count() == 1:
        return pack(interface_id,"30011","地址重复")
    if Warehouse.objects.filter(id = warehouse_id).count() == 1:
        return pack(interface_id,"30012","仓库号重复")
    tmpWarehouse = Warehouse.objects.create(
        id = warehouse_id,
        address = address,
    )
    resp = {
        "warehouse":[tmpware.toDict() for tmpware in Warehouse.objects.all()]
    }
    return pack(interface_id,data = resp)

@admin
@post
def modify_address(request):
    interface_id = "3002"
    warehouse_id = request.POST.get("warehouse_id",None)
    new_address = request.POST.get("new_address",None)
    if not warehouse_id:
        return pack(interface_id,"110","参数非法")
    if Warehouse.objects.filter(id = warehouse_id).count() == 0:
        return pack(interface_id,"30021","仓库号不存在")
    if not new_address:
        Warehouse.objects.get(id = warehouse_id).toDelete()
        resp = {
            "warehouse":[itr.toDict() for itr in Warehouse.objects.all()]
        }
        return pack(interface_id,data = resp)
    else:
        tmp = Warehouse.objects.get(id = warehouse_id)
        tmp.address = new_address
        tmp.save()
        rsp = {
            "warehouse":[itr.toDict() for itr in Warehouse.objects.all()]
        }
        return pack(interface_id,data = rsp)

@admin
@get
def get_cargoin(request):
    interface_id = "3010"
    goods_id = request.GET.get("goods_id",None)
    warehouse_id = request.GET.get("warehouse_id",None)
    if warehouse_id:
        try:
            flag = Cargoin.objects.get(warehouse_id = warehouse_id)
        except Exception as e:
            return pack(interface_id, "30102", "仓库不存在")
        rsp = {
            "warehouse":[cargo.toDict() for cargo in Cargoin.objects.filter(warehouse_id = warehouse_id)]
        }
        return pack(interface_id, data = rsp)
    else:
        if goods_id:
            try:
                flag = Cargoin.objects.get(goods_id = goods_id)
            except Exception as e1:
                return pack(interface_id, "30101", "商品不存在")
            rsp = {
                "warehouse":[cargo.toDict() for cargo in Cargoin.objects.filter(goods_id = goods_id)]
            }
            return pack(interface_id, data = rsp)
        else:
            rsp = {
                "warehouse":[cargo.toDict() for cargo in Cargoin.objects.all()]
            }
    return

@admin
@post
def add_cargoin(request):
    interface_id = "3011"
    goods_id = request.POST.get("goods_id",None)
    warehouse_id = request.POST.get("warehouse_id",None)
    amount = request.POST.get("amount",None)
    cost = request.POST.get("cost",None)
    shelflife = request.POST.get("cost",None)
    reason = request.POST.get("reason","Default")
    if((not goods_id) or (not warehouse_id) or (not amount) or (not cost) ):
        return pack(interface_id, "110", "参数非法")
    
    try:
        tmp = Goods.objects.get(goods_id = goods_id)
    except Exception as e0:
        return pack(interface_id, "30111", "商品不存在")

    try:
        tmp = Warehouse.objects.get(warehouse_id = warehouse_id)
    except Exception as e0:
        return pack(interface_id, "30111", "仓库不存在")
    
    flag = False
    amountint = 0
    costint = 0
    shelflifeint = 0
    if not shelflife:
        shelflifeint = 72
    else:
        try:
            shelflifeint = int(shelflife)
            if(shelflifeint == 0):
                shelflifeint = 72
            if(shelflifeint < 0):
                flag = True
        except Exception as e:
            flag = True
    
    if(flag):
        return pack(interface_id, "30115", "非法shelflife")

    flag = False
    try:
        amountint = int(amount)
        if(amountint <= 0):
            flag = True
    except Exception as e:
        flag = True
    
    if(flag):
        return pack(interface_id, "30113", "非法amount")
    
    flag = False
    
    try:
        costint = int(cost)
        if(cost < 0):
            flag = True
    except Exception as e:
        flag = True
    
    if(flag):
        return pack(interface_id, "30114", "非法cost")
    
    flag = False
    entrytime = datetime.datetime.now().astimezone(pytz.timezone("Asia/Shanghai"))
    staletime = entrytime + datetime.timedelta(hours = shelflifeint)
    try:
        cargoin = Cargoin.objects.create(
            goods_id = goods_id,
            warehouse_id = warehouse_id,
            amount = amountint,
            cost = costint,
            entrytime = entrytime,
            shelflife = shelflifeint,
            staletime = staletime,
            reason = reason,
        )
        cargoin.save()
    except Exception as ec:
        print(ec)
        return pack(interface_id,"null","添加进货单失败，未知")
    
    return pack(interface_id,data = {})
    
    