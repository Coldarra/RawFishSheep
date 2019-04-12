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
                return pack(interface_id, "20013", "图片不存在")
        return pack(interface_id, "0", "成功", resp)

@post
# @admin
def setting(request):
    interface_id = "2002"
    goods_id = Goods.POST.get("goods_id", None)
    key = Goods.POST.get("key", None)
    value = Goods.POST.get("value", None)

    try:
        goods = Goods.objects.get(id=goods_id)
        