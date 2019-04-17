from django.shortcuts import render
from decorator import *
from django.http import HttpResponse
# Create your views here.

@get
def test(request):
    return HttpResponse('OK')

@admin
@get
def get_warehouseinfo(request):
    interface_id = "3000"
    resp = {
        "warehouse":[tmpware.toDirt() for tmpware in Warehouse.objects.all()]
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
