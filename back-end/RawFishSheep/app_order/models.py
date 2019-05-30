from django.db import models
from app_user.models import *
from app_goods.models import *
# Create your models here.


class Order(models.Model):
    serialnumber = models.CharField(
        default='0', max_length=50, verbose_name='序列号')
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.DO_NOTHING, related_name='orders_by_user')
    address = models.ForeignKey(Address, null=True, blank=True,
                                on_delete=models.DO_NOTHING, related_name='orders_by_address', verbose_name='收货地址')
    totalprice = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='订单总价')
    discount = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='优惠价格')
    createtime = models.DateTimeField(auto_now_add=True,
                                      blank=True, null=True, verbose_name='下单时间')

    paidtime = models.DateTimeField(blank=True, null=True, verbose_name='支付时间')
    paymentname = models.CharField(
        default='货到付款', max_length=20, verbose_name='付款渠道')

    finishtime = models.DateTimeField(
        blank=True, null=True, verbose_name='完成时间')
    isrefund = models.CharField(
        default='0', max_length=1, verbose_name='是否完成退款')

    status = models.CharField(
        default='unprocessed', max_length=20, verbose_name='订单状态')
    # status  代支付 未处理订单  审核中订单 2:配货中订单 3: 配送中订单 4:已完成配送 5:用户确认收货
    # processing, examining, preparing, delivering, delivered, confirmed,
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Order__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        status_mapping = {
            "0": "processing",
            "1": "examining",
            "2": "preparing",
            "3": "delivering",
            "4": "delivered",
            "5": "confirmed",
        }

        return {
            "id": self.id,
            "serialnumber": self.serialnumber,
            "user": self.user.username,
            "address": self.address.address,
            "totalprice": "¥{:.2f}".format(self.totalprice/100),
            "discount": self.discount,
            "createtime": self.createtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "finishtime": self.finishtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S") if self.finishtime else "",
            "paidtime": self.paidtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S") if self.finishtime else "",
            "paymentname": self.paymentname,
            "isrefund": self.isrefund,
            "isdelete": self.isdelete,
            "status": self.status,
            "detail": [orderdetail.toDict() for orderdetail in self.detail_by_order.all()]
        }

    class Meta:
        db_table = 'order'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='detail_by_order')
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='detail_by_goods')
    price = models.IntegerField(
        default=0, verbose_name='单价')
    amount = models.IntegerField(
        default=0, verbose_name='数量')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__OrderDetail__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "order": self.order.id,
            "goods_id": self.goods_id,
            "goods": self.goods.toDict(),
            "amount": self.amount,
            "price": "{:.2f}".format(self.price/100),
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'order_detail'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'
