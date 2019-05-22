
from .models import *
from decorator import *
from . import views
from django.shortcuts import render
from django.http import HttpResponse



@service
def get_goods_info(param):  # 获取商品信息
    interface_id = "2000"
    goods_id = param.get('goods_id', None)
    try:
        goods = views.getGoodsByID(goods_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
    resp = {
            "goods": goods.toDict(),
        }
    return pack(interface_id, data=resp)


@service
def get_all_goods(param):
    interface_id = "2003"
    resp = {
        "goods": [goods.toDict() for goods in views.getAllGoods()]
    }
    return pack(interface_id, data = resp)


@login
@service
def append(param):  # 添加商品（不捣乱的管理员）
    interface_id = "2001"
    name = param.get("name", None)
    category_id = param.get("category_id", None)
    picture_id = param.get("picture_id", None)
    unit = param.get("unit", None)
    price = param.get("price", None)
    remain = param.get("remain", None)

    try:
        goods = Goods.objects.get(name=name, isdelete="0")
        return pack(interface_id, "20012", "商品名重复")
    except:
        pass
    if not remain:
        remain = 0
    goods = Goods.objects.create(
        name=name,
        category_id=category_id,
        unit=unit,
        price=price,
        remain=remain,
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
@admin
def setting(param):  # 修改商品
    interface_id = "2002"
    goods_id = param.get("goods_id", None)
    key = param.get("key", None)
    value = param.get("value", None)

    if key == None or value == None:
        return pack(interface_id, "110", "参数非法")

    if key not in ["category_id", "name", "unit", "status", "price", "remain", ]:
        return pack(interface_id, "20023", "参数异常")

    try:
        goods = Goods.objects.get(id=goods_id, isdelete="0")
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
@admin
def delete(param):  # 删除商品
    interface_id = "2004"
    goods_id = param.get("goods_id", None)

    try:
        goods = Goods.objects.get(id=goods_id)
        goods.toDelete()
        return pack(interface_id)
    except:
        return pack(interface_id, "20042", "商品不存在")


@get
def get_category(param):  # 获取所有分类
    interface_id = "2010"

    try:
        resp = {"category": []}
        count = 0
        for categoryi in Category.objects.filter(level=1, isdelete="0"):
            category1 = {
                "value": categoryi.id,
                "label": categoryi.name,
                "level": categoryi.level,
                "children": [],
            }
            resp["category"].append(category1)
            for categoryj in Category.objects.filter(superior=categoryi.id, isdelete="0"):
                category2 = {
                    "value": categoryj.id,
                    "label": categoryj.name,
                    "level": categoryj.level,
                    "children": [],
                }
                resp["category"][-1]["children"].append(category2)
                for categoryk in Category.objects.filter(superior=categoryj.id, isdelete="0"):
                    category3 = {
                        "value": categoryk.id,
                        "label": categoryk.name,
                        "level": categoryk.level,
                    }
                    resp["category"][-1]["children"][-1]["children"].append(
                        category3)
                if len(resp["category"][-1]["children"][-1]["children"]) == 0:
                    del resp["category"][-1]["children"][-1]["children"]
            if len(resp["category"][-1]["children"]) == 0:
                del resp["category"][-1]["children"]
        return pack(interface_id, "0", "成功", resp)
    except:
        pass


@post
@admin
def append_category(param):  # 添加分类
    interface_id = "2011"
    name = param.get("name", None)
    superior = param.get("superior_id", None)

    try:
        category0 = Category.objects.get(name=name, isdelete="0")
        return pack(interface_id, "20112", "分类名重复")
    except:
        pass
    try:
        category1 = Category.objects.get(id=eval(superior))
        category = Category.objects.create(
            name=name,
            superior=eval(superior),
            level=category1.level+1,
        )
        resp = {
            "category": category.toDict(),
        }
        return pack(interface_id, "0", "成功", resp)
    except:
        pass


@post
@admin
def setting_category(param):  # 修改分类名称
    interface_id = "2012"
    category_id = param.get("category_id", None)
    name = param.get("name", None)

    if name == None:
        return pack(interface_id, "110", "参数非法")

    try:
        category = Category.objects.get(id=category_id, isdelete="0")
        try:
            category0 = Category.objects.get(name=name)
            return pack(interface_id, "20123", "分类名重复")
        except:
            category.name = name
        category.save()
        resp = {
            "category": category.toDict(),
        }
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "20122", "无此分类")


@post
@admin
def delete_category(param):  # 删除分类
    interface_id = "2013"
    category_id = param.get("category_id", None)

    try:
        category = Category.objects.get(id=category_id)
        category.toDelete()
        return pack(interface_id)
    except:
        return pack(interface_id, "20132", "无此分类")


@get
def get_picture(param):  # 获取商品图片
    interface_id = "2020"
    goods_id = param.GET.get("goods_id", None)

    try:
        goods = Goods.objects.get(id=goods_id, isdelete="0")
        l1 = goods.picture_by_goods.filter(isdelete="0")
        if len(l1) == 0:
            return pack(interface_id, "20203", "图片查询无果")
        resp = {
            "picture": []
        }
        for picture in l1:
            resp["picture"].append(picture.toDict())
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "20202", "无效商品")

# @post
# @admin
# def append_picture(param):
#     interface_id = "2021"
#     goods_id = param.get("goods_id", None)
#     picture_id = param.get("picture_id", None)

#     try:
#         goods = Goods.objects.get(id=goods_id, isdelete="0")
#         try:
#             picture = Picture.objects.get(id=picture_id, isdelete="0")
#             picture.goods = goods
#             resp {
#                 "picture": picture.toDict(),
#             }
#             return pack(interface_id, "0", "成功", resp)
#         except:
#             return pack(interface_id, "20213", "无效图片")
#     except:
#         return pack(interface_id, "20212", "无效商品")


@post
@admin
def delete_picture(param):  # 删除商品图片
    interface_id = "2022"
    picture_id = param.get("picture_id", None)

    try:
        picture = Picture.objects.get(id=picture_id)
        picture.toDelete()
        return pack(interface_id)
    except:
        return pack(interface_id, "20223", "无效图片")
