from django.db import models
from app_order.models import *
from app_user.models import *
from app_goods.models import *
# Create your models here.
import pytz


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.DO_NOTHING, related_name='cart_by_user')
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='cart_by_goods')
    amount = models.IntegerField(default=0, verbose_name='数量')
    selection = models.CharField(
        default='1', max_length=1, verbose_name='是否勾选')
    createtime = models.DateTimeField(auto_now=True,
                                      blank=True, null=True, verbose_name='创建时间')

    def __str__(self):
        text = "__Cart__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "goodsid": self.goods_id,
            "goods": self.goods.name,
            "amount": self.amount,
            "selection": self.selection,
        }

    class Meta:
        db_table = 'order_cart'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'
