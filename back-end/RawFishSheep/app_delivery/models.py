from django.db import models
from app_order.models import *
from app_user.models import *
# Create your models here.


class Delivery(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='delivery_by_order')
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.DO_NOTHING, related_name='delivery_by_user')
    createtime = models.DateTimeField(
        blank=True, null=True, verbose_name='配送单创建时间')
    receivetime = models.DateTimeField(
        blank=True, null=True, verbose_name='接货时间')
    finishtime = models.DateTimeField(
        blank=True, null=True, verbose_name='送达时间')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Delivery__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "order": self.order_id,
            "user": self.user.username,
            "createtime": self.createtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "receivetime": self.receivetime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S") if self.receivetime else None,
            "finishtime": self.finishtime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S") if self.finishtime else None,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'order_delivery'
        verbose_name = 'RawFishSheep'
        app_label = 'app_order'
