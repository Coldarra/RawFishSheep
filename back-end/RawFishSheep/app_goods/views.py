
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def getGoodsByID(goods_id=None):
    if goods_id == None:
        raise ParamException()
    if Goods.objects.filter(id=goods_id, isdelete="0").count():
        goods = Goods.objects.get(id=goods_id, isdelete="0")
    else:
        raise RFSException("20002", "商品不存在")
    return goods


def getGoodsByName(name=None):
    if name == None:
        raise ParamException()
    if Goods.objects.filter(name=name, isdelete="0").count():
        raise RFSException("20012", "商品名重复")


def getAllGoods():
    return Goods.objects.filter(isdelete="0")


def getGoodsByCategory(category_id=None):
    pass


def createGoods(name=None, category_id=None, unit=None, price=None, remain=None):
    getGoodsByName(name)

    if None in [name, category_id, unit, price, remain]:
        raise ParamException()
    goods = Goods.objects.create(
        name=name,
        category_id=category_id,
        unit=unit,
        price=price,
        remain=remain,
    )
    return goods


def changeGoodsInfo(goods_id, key, value):
    goods = getGoodsByID(goods_id)

    if None in [key, value]:
        raise ParamException()

    if key not in ["category_id", "name", "unit", "status", "price", "remain", ]:
        raise RFSException("20023", "参数异常")

    if key == "category_id":
        goods.category_id = value
    elif key == "name":
        goods.name = value
    elif key == "unit":
        goods.unit = value
    elif key == "status":
        goods.status = value
    elif key == "price":
        goods.price = value
    elif key == "remain":
        goods.remain = value
    goods.save()
    return goods


def deleteGoods(goods_id):
    goods = getGoodsByID(goods_id)
    goods.toDelete()
    return goods


def getAllCategory():
    data = []
    for categoryi in Category.objects.filter(level=1, isdelete="0"):
            category1 = {
                "value": categoryi.id,
                "label": categoryi.name,
                "level": categoryi.level,
                "children": [],
            }
            data.append(category1)
            for categoryj in Category.objects.filter(superior=categoryi.id, isdelete="0"):
                category2 = {
                    "value": categoryj.id,
                    "label": categoryj.name,
                    "level": categoryj.level,
                    "children": [],
                }
                data[-1]["children"].append(category2)
                for categoryk in Category.objects.filter(superior=categoryj.id, isdelete="0"):
                    category3 = {
                        "value": categoryk.id,
                        "label": categoryk.name,
                        "level": categoryk.level,
                    }
                    data[-1]["children"][-1]["children"].append(
                        category3)
                if len(data[-1]["children"][-1]["children"]) == 0:
                    del data[-1]["children"][-1]["children"]
            if len(data[-1]["children"]) == 0:
                del data[-1]["children"]
    return data


def getCategoryByID(category_id):
    if category_id == None:
        raise ParamException()
    if Category.objects.filter(id=category_id, isdelete="0").count():
        category = Category.objects.get(id=category_id, isdelete="0")
    else:
        raise RFSException("20113", "分类不存在")
    return category


def getCategoryByname(name):
    if name == None:
        raise ParamException()
    if Category.objects.filter(name=name, isdelete="0").count():
        raise RFSException("20112", "分类名重复")


def createCategory(name, superior_id):
    getCategoryByname(name)
    if None in [name, superior_id]:
        raise ParamException()
    category1 = getCategoryByID(superior_id)
    category = Category.objects.create(
        name=name,
        superior=superior_id,
        level=category1.level+1,
    )
    return category


def changeCategory(category_id, name):
    category = getCategoryByID(category_id)

    if name == None:
        raise ParamException()

    getCategoryByname(name)
    category.name = name
    category.save()
    return category


def deleteCategory(category_id):
    category = getCategoryByID(category_id)
    category.toDelete()
    return category


def getPictureByGoods(goods_id):
    pass


def getPictureByID(picture_id):
    if picture_id == None:
        raise ParamException()
    if Picture.objects.filter(id=picture_id).count():
        picture = Picture.objects.get(id=picture_id)
    else:
        raise RFSException("20013", "图片不存在")
    return picture


def createPicture():
    pass


def deletePicture(picture_id):
    pass
