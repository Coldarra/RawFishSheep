from django.db import models
from app_user.models import *
from app_goods.models import *
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='orders_by_user')
    address = models.ForeignKey(Address, null=True, blank=True,
                                on_delete=models.SET_NULL, related_name='orders_by_address')
    totalprice = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='订单总价')
    discount = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='优惠价格')
    createtime = models.DateTimeField(
        blank=True, null=True, verbose_name='下单时间')
    finishtime = models.DateTimeField(
        blank=True, null=True, verbose_name='完成时间')
    isrefund = models.CharField(max_length=1, verbose_name='是否完成退款')
    isdelete = models.CharField(max_length=1, verbose_name='是否删除', default='0')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.user, self.address, self.totalprice, self.discount, self.createtime, self.finishtime, self.isrefund, self.isdelete)

    def toDict(self):
        return {
            "id": self.id,
            "user": self.user,
            "address": self.address,
            "totalprice": self.totalprice,
            "discount": self.discount,
            "createtime": self.createtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "finishtime": self.finishtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "isrefund": self.isrefund,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'order'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='detail_by_order')
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='detail_by_goods')
    price = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='价格')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        return "{} {} {} {}".format(self.order, self.goods, self.price, self.isdelete)

    def toDict(self):
        return {
            "id": self.id,
            "order": self.order,
            "goods": self.goods,
            "price": self.price,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'order_detail'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='cart_by_user')
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='cart_by_goods')
    amount = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='数量')
    price = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='价格')
    selection = models.CharField(
        default='1', max_length=1, verbose_name='是否勾选')

    def __str__(self):
        return "{} {} {} {} {}".format(self.user, self.goods, self.amount, self.price, self.selection)

    def toDict(self):
        return {
            "id": self.id,
            "user": self.user,
            "goods": self.goods,
            "amount": self.amount,
            "price": self.price,
            "selection": self.selection,
        }

    class Meta:
        db_table = 'order_cart'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'
