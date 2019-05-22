
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse

def getGoodsByID(goods_id=None):
    if goods_id == None:
        raise ParamException()
    if Goods.objects.get(id=goods_id, isdelete="0").count():
        goods = Goods.objects.get(id=goods_id, isdelete="0")
    else:
        raise RFSException("20002", "商品不存在")
    return goods


def getGoodsByCategory(category_id=None):
    pass


def createGoods(name=None, category_id=None, unit=None, price=None, remain=None):
    pass


def changeGoodsInfo(goods_id, key, value):
    goods = getGoodsByID(goods_id)


def deleteGoods(goods_id):
    pass


def getAllCategory():
    pass


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
    pass


def createPicture():
    pass


def deletePicture(picture_id):
    pass
