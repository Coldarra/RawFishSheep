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
    interface_id = 2000
    goods_id = request.GET.get('goods_id', None)

    try:
        goods = Goods.objects.get(id=goods_id)
        rsp = {
            "goods": goods.toDict()
        }
        return pack(interface_id, "0", "成功", rsp)
    except:
        return pack(interface_id, "20002", "商品不存在")

# @post
# @admin
# def append(request):
#     interface_id = 2001
#     name = request.POST.get("name", None)
#     category_id = request.POST.get("category_id", None)
#     picture_id = request.POST.get("picture_id", None)

#     try:
#         goods = Goods.objects.get(name=name)
#         return pack(interface_id, "20012", "商品名重复")
#     except:
