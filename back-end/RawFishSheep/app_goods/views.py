from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse

import sys
sys.path.append('../')


@get
def test(request):
    return HttpResponse('OK')


@get
def info(request):
    interface_id = "2000"
    goods_id = request.GET.get('goods_id', None)

    try:
        goods = Goods.objects.get(id=goods_id)
        resp = {
            "goods": goods.toDict(),
        }
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "20002", "商品不存在")

@post
# @admin
def append(request):
    interface_id = "2001"
    name = request.POST.get("name", None)
    category_id = request.POST.get("category_id", None)
    picture_id = request.POST.get("picture_id", None)

    try:
        goods = Goods.objects.get(name=name)
        return pack(interface_id, "20012", "商品名重复")
    except:
        goods = Goods.objects.create(
            name=name,
            category_id=category_id,
        )
        resp = {
            "goods": goods.toDict(),
        }
        if not picture_id:
            try:
                picture = Picture.objects.get(id=picture_id)
                picture.goods = goods
            except:
                pass
        return pack(interface_id, "0", "成功", resp)

@post
# @admin
def setting(request):
    interface_id = "2002"
    goods_id = Goods.POST.get("goods_id", None)
    key = Goods.POST.get("key", None)
    value = Goods.POST.get("value", None)

    if key == None or value == None:
        return pack(interface_id, "110", "参数非法")

    if key not in ["category", "name", "unit", "status", "price", "remain", "isdelete"]:
        return pack(interface_id, "10042", "未知属性")

    try:
        goods = Goods.objects.get(id=goods_id)
        if key == "category":
            goods.category_id = value
        if key == "name":
            goods.name = value
        if key == "unit":
            goods.unit = value
        if key == "status":
            goods.status = value
        if key == "price":
            goods.price = value
        if key == "remain":
            goods.remain = value
        goods.save()
        resp = {
            "goods": goods.toDict(),
        } 
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "20022", "商品不存在")


@post
# @admin
def delete(request):
    interface_id = "2004"
    goods_id = Goods.POST.get("goods_id", None)

    try:
        goods_id = Goods.objects.get(id=goods_id)
        
    except:
        return pack(interface_id, "20042", "商品不存在")