
from . import views
from .models import *
from app_user.views import *


def getGoodsByID(goods_id=None):
    pass


def getGoodsByCategory(category_id=None):
    pass


def createGoods(name=None, category_id=None, unit=None, price=None, remain=None):
    pass


def changeGoodsInfo(goods_id, key, value):
    pass


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
