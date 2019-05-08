from django.shortcuts import render
from decorator import *
from django.http import HttpResponse

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
        "warehouse": [tmpware.toDict() for tmpware in Warehouse.objects.all()]
    }
    return pack(interface_id, data=resp)


@admin
@post
def append_warehouse(request):
    interface_id = "3001"
    address = request.POST.get("address", None)
    if not address:
        return pack(interface_id, "110", "参数非法")
    if Warehouse.objects.filter(address=address).count() == 1:
        return pack(interface_id, "30011", "地址重复")
    tmpWarehouse = Warehouse.objects.create(address=address,)
    resp = {
        "warehouse": [tmpware.toDict() for tmpware in Warehouse.objects.all()]
    }
    return pack(interface_id, data=resp)


@admin
@post
def modify_address(request):
    interface_id = "3002"
    warehouse_id = request.POST.get("warehouse_id", None)
    new_address = request.POST.get("new_address", None)
    if not warehouse_id:
        return pack(interface_id, "110", "参数非法")
    if Warehouse.objects.filter(id=warehouse_id).count() == 0:
        return pack(interface_id, "30021", "仓库号不存在")
    if not new_address:
        Warehouse.objects.get(id=warehouse_id).toDelete()
        resp = {
            "warehouse": [itr.toDict() for itr in Warehouse.objects.all()]
        }
        return pack(interface_id, data=resp)
    else:
        tmp = Warehouse.objects.get(id=warehouse_id)
        tmp.address = new_address
        tmp.save()
        rsp = {
            "warehouse": [itr.toDict() for itr in Warehouse.objects.all()]
        }
        return pack(interface_id, data=rsp)


@admin
@post
def delete_address(request):
    interface_id = "3003"


@admin
@get
def get_cargoin_info(request):
    interface_id = "3010"
    goods_id = request.GET.get("goods_id", None)
    warehouse_id = request.GET.get("warehouse_id", None)

    if goods_id:
        if warehouse_id:
            cargoins = Cargoin.objects.filter(
                goods_id=goods_id, warehouse_id=warehouse_id)
        else:
            cargoins = Cargoin.objects.filter(goods_id=goods_id)
    else:
        if warehouse_id:
            cargoins = Cargoin.objects.filter(warehouse_id=warehouse_id)
        else:
            cargoins = Cargoin.objects.all()
    if len(cargoins) == 0:
        if goods_id:
            return pack(interface_id, "30101", "商品不存在")
        if warehouse_id:
            return pack(interface_id, "30102", "仓库不存在")
    resp = {
        "warehouse": [cargoin.toDict() for cargoin in cargoins]
    }
    print(cargoins)
    return pack(interface_id, data=resp)
    # if warehouse_id:
    #     try:
    #         flag = Cargoin.objects.get(warehouse_id=warehouse_id)
    #     except Exception as e:
    #         return pack(interface_id, "30102", "仓库不存在")
    #     rsp = {
    #         "warehouse": [cargo.toDict() for cargo in Cargoin.objects.filter(warehouse_id=warehouse_id)]
    #     }
    #     return pack(interface_id, data=rsp)
    # else:
    #     if goods_id:
    #         try:
    #             flag = Cargoin.objects.get(goods_id=goods_id)
    #         except Exception as e1:
    #             return pack(interface_id, "30101", "商品不存在")
    #         rsp = {
    #             "warehouse": [cargo.toDict() for cargo in Cargoin.objects.filter(goods_id=goods_id)]
    #         }
    #         return pack(interface_id, data=rsp)
    #     else:
    #         rsp = {
    #             "warehouse": [cargo.toDict() for cargo in Cargoin.objects.all()]
    #         }
    # return


@admin
@post
def append_cargoin(request):
    interface_id = "3011"
    print("interface_id:", interface_id)
    goods_id = request.POST.get("goods_id", None)
    warehouse_id = request.POST.get("warehouse_id", None)
    amount = request.POST.get("amount", None)
    cost = request.POST.get("cost", None)
    shelflife = request.POST.get("shelflife", None)
    reason = request.POST.get("reason", None)
    print("goods_id:", goods_id)
    if not goods_id:
        return pack(interface_id, "110", "缺少参数goods_id")
    if not warehouse_id:
        return pack(interface_id, "110", "缺少参数warehouse_id")
    if Goods.objects.filter(id=goods_id).count() == 0:
        return pack(interface_id, "30111", "商品不存在")
    if Warehouse.objects.filter(id=warehouse_id).count() == 0:
        return pack(interface_id, "30112", "商品不存在")
    try:
        if int(amount) < 0:
            return pack(interface_id, "30113", "amount<0")
    except:
        return pack(interface_id, "30113", "amount不可转换为int")
    try:
        if int(cost) < 0:
            return pack(interface_id, "30114", "cost<0")
    except:
        return pack(interface_id, "30114", "amount不可转换为int")
    if shelflife:
        try:
            if int(shelflife) < 0:
                return pack(interface_id, "30115", "shelflife<0")
        except:
            return pack(interface_id, "30115", "shelflife不可转换为int")

    try:
        cargoin = Cargoin.objects.create(
            goods_id=goods_id,
            warehouse_id=warehouse_id,
            amount=amount,
            cost=cost,
        )
        if reason:
            cargoin.reason = reason
            cargoin.save()
    except Exception as e:
        print(e)
        return pack(interface_id, "30119", "数据库写入失败"+str(e))

    if not shelflife:
        shelflife = cargoin.shelflife
    else:
        cargoin.shelflife = int(shelflife)
    timenow = datetime.datetime.now()
    staletime = timenow + datetime.timedelta(hours=int(shelflife))

    cargoin.entrytime = timenow
    cargoin.staletime = staletime
    cargoin.save()

    return pack(interface_id, {"cargoin": cargoin.toDict()})

    # if((not goods_id) or (not warehouse_id) or (not amount) or (not cost)):
    #     return pack(interface_id, "110", "参数非法")

    # try:
    #     tmp = Goods.objects.get(goods_id=goods_id)
    # except Exception as e:
    #     return pack(interface_id, "30111", "商品不存在")

    # try:
    #     tmp = Warehouse.objects.get(warehouse_id=warehouse_id)
    # except Exception as e0:
    #     return pack(interface_id, "30111", "仓库不存在")

    # flag = False
    # amountint = 0
    # costint = 0
    # shelflifeint = 0
    # if not shelflife:
    #     shelflifeint = 72
    # else:
    #     try:
    #         shelflifeint = int(shelflife)
    #         if(shelflifeint == 0):
    #             shelflifeint = 72
    #         if(shelflifeint < 0):
    #             flag = True
    #     except Exception as e:
    #         flag = True

    # if(flag):
    #     return pack(interface_id, "30115", "非法shelflife")

    # flag = False
    # try:
    #     amountint = int(amount)
    #     if(amountint <= 0):
    #         flag = True
    # except Exception as e:
    #     flag = True

    # if(flag):
    #     return pack(interface_id, "30113", "非法amount")

    # flag = False

    # try:
    #     costint = int(cost)
    #     if(cost < 0):
    #         flag = True
    # except Exception as e:
    #     flag = True

    # if(flag):
    #     return pack(interface_id, "30114", "非法cost")

    # flag = False
    # entrytime = datetime.datetime.now().astimezone(pytz.timezone("Asia/Shanghai"))
    # staletime = entrytime + datetime.timedelta(hours=shelflifeint)
    # try:
    #     cargoin = Cargoin.objects.create(
    #         goods_id=goods_id,
    #         warehouse_id=warehouse_id,
    #         amount=amountint,
    #         cost=costint,
    #         entrytime=entrytime,
    #         shelflife=shelflifeint,
    #         staletime=staletime,
    #         reason=reason,
    #     )
    # except Exception as ec:
    #     print(ec)
    #     return pack(interface_id, "null", "添加进货单失败，未知")

    # return pack(interface_id, data={})
