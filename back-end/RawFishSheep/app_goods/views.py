
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


def deleteGoods(goods_id):
    pass


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
    pass


def createCategory(balala):
    pass


def changeCategory(category_id, key, value):
    pass


def deleteCategory(category_id):
    pass


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
