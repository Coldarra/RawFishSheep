
from .models import *
from decorator import *
from .views import *
from django.shortcuts import render
from django.http import HttpResponse



@service
def get_goods_info(param):  # 获取商品信息
    interface_id = "2000"
    goods_id = param.get('goods_id', None)
    try:
        goods = getGoodsByID(goods_id)
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
        "goods": [goods.toDict() for goods in getAllGoods()]
    }
    return pack(interface_id, data = resp)


@login
@service
def create_goods(param):  # 添加商品（不捣乱的管理员）
    interface_id = "2001"
    name = param.get("name", None)
    category_id = param.get("category_id", None)
    picture_id = param.get("picture_id", None)
    unit = param.get("unit", None)
    price = param.get("price", None)
    remain = param.get("remain", None)
    
    if not remain:
        remain = 0
    try:
        goods = createGoods(name, category_id, unit, price, remain)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))

    resp = {
        "goods": goods.toDict()
    }
    if picture_id:
        try:
            picture = getPictureByID(goods_id)
        except RFSException as e:
            return pack(interface_id, e.ret, e.msg)
        except Exception as e:
            return pack(interface_id, interface_id+"1", str(e))
        picture.goods = goods

    return pack(interface_id, data=resp)


@login
@service
def change_goods(param):  # 修改商品
    interface_id = "2002"
    goods_id = param.get("goods_id", None)
    key = param.get("key", None)
    value = param.get("value", None)

    try:
        goods = changeGoodsInfo(goods_id, key, value)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
    
    resp = {
        "goods": goods.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def delete_goods(param):  # 删除商品
    interface_id = "2004"
    goods_id = param.get("goods_id", None)

    try:
        goods = deleteGoods(goods_id)
        return pack(interface_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))


@service
def get_category(param):  # 获取所有分类
    interface_id = "2010"
    try:
        resp = {
            "category": getAllCategory()
        }
        return pack(interface_id, data=resp)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))


@login
@service
def create_category(param):  # 添加分类
    interface_id = "2011"
    name = param.get("name", None)
    superior = param.get("superior_id", None)

    try:
        category = createCategory(name, superior)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))

    resp = {
        "category": category.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def change_category(param):  # 修改分类名称
    interface_id = "2012"
    category_id = param.get("category_id", None)
    name = param.get("name", None)

    try:
        category = changeCategory(category_id, name)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
    resp = {
        "category": category.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def delete_category(param):  # 删除分类
    interface_id = "2013"
    category_id = param.get("category_id", None)

    try:
        deleteCategory(category_id)
        return pack(interface_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))


@service
def get_picture(param):  # 获取商品图片
    interface_id = "2020"
    goods_id = param.get("goods_id", None)

    try:
        gp = getPictureByGoods(goods_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
    resp = {
        "picture": [gp1.toDict for gp1 in gp]
    }
    return pack(interface_id, data=resp)

@login
@service
def append_picture(param):
    interface_id = "2021"
    goods_id = param.get("goods_id", None)
    picture_id = param.get("picture_id", None)

    try:
        goods = getGoodsByID(goods_id)
        picture = getPictureByID(picture_id)
        picture.goods = goods
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
    resp = {
        "picture": picture.toDict(),
    }
    return pack(interface_id, data=resp)


@login
@service
def delete_picture(param):  # 删除商品图片
    interface_id = "2022"
    picture_id = param.get("picture_id", None)

    try:
        deletePicture(picture_id)
        return pack(interface_id)
    except RFSException as e:
        return pack(interface_id, e.ret, e.msg)
    except Exception as e:
        return pack(interface_id, interface_id+"0", str(e))
