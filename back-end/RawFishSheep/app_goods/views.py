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
    goods_id = request.POST.get("goods_id", None)
    key = request.POST.get("key", None)
    value = request.POST.get("value", None)

    if key == None or value == None:
        return pack(interface_id, "110", "参数非法")

    if key not in ["category_id", "name", "unit", "status", "price", "remain",]:
        return pack(interface_id, "20023", "参数异常")

    try:
        goods = Goods.objects.get(id=goods_id)
        if key == "category_id":
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
    goods_id = request.POST.get("goods_id", None)

    try:
        goods = Goods.objects.get(id=goods_id)
        goods.toDelete()
        return pack(interface_id)
    except:
        return pack(interface_id, "20042", "商品不存在")

@get
def get_category(request):
    interface_id = "2010"

    try:
        resp = {"category": []}
        for categoryi in Category.obejects.get(level=1):
            category1 = {
                "value":categoryi.id,
                "label":categoryi.name,
                "level":categoryi.level,
                "children":[],
            }
            resp[category].append(category1)
            for categoryj in Category.objects.get(superior_id=categoryi.id):
                category2 = {
                    "value":categoryj.id,
                    "label":categoryj.name,
                    "level":categoryj.level,
                    "children":[],
                }
                resp[category][children].append(category2)
                for categoryk in Category.objects.get(superior_id=categoryj.id):
                category3 = {
                    "value":categoryk.id,
                    "label":categoryk.name,
                    "level":categoryk.level,
                }
                resp[category][children][children].append(category3)
        return pack(interface_id, "0", "成功", resp)
    except:
        pass

@post
# @admin
def append_category(request):
    interface_id = "2011"
    name = request.POST.get("name", None)
    superior_id = request.POST.get("superior_id", None)

    try:
        category = Category.objects.get(name=name)
        return pack(interface_id, "20112", "分类名重复")
    except:
        category = Category.objects.create(
            name=name,
            superior_id=superior_id,
        )
        resp = {
            "category": category.toDict(),
        }
        return pack(interface_id, "0", "成功", resp)

@post
# @admin
def setting_category(request):
    interface_id = "2012"
    category_id = request.POST.get("category_id", None)
    key = request.POST.get("key", None)
    value = request.POST.get("value", None)

    if key == None or value == None:
        return pack(interface_id, "110", "参数非法")

    if key not in ["name"]:
        return pack(interface_id, "20125", "参数异常")

    try:
        category = Category.objects.get(id=category_id)
        if key == "name":
            try:
                name = Category.objects.get(name=value)
                return pack(interface_id, "20123", "分类名重复")
            except:
                category.name = value
        category.save()
        resp = {
            "category": category.toDict(),
        } 
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "20122", "无此分类")