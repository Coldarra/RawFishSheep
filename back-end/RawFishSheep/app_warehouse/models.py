from django.db import models
from app_user.models import *
from app_order.models import *
from app_goods.models import *

# Create your models here.


class Warehouse(models.Model):
    address = models.CharField(max_length=300, verbose_name='仓库地址')

    def __str__(self):
        text = "__Warehouse__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return textmat(self.address)

    def toDict(self):
        return {
            "id": self.id,
            "address": self.address,
        }

    class Meta:
        db_table = 'warehouse'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'


class Cargoin(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='cargoin_by_goods')
    warehouse = models.ForeignKey(Warehouse, null=True, blank=True,
                                  on_delete=models.SET_NULL, related_name='cargoin_by_warehouse')
    amount = models.IntegerField(blank=True, null=True, verbose_name='进货量')
    cost = models.IntegerField(blank=True, null=True, verbose_name='进货成本')
    entrytime = models.DateTimeField(
        blank=True, null=True, verbose_name='入库时间')
    staletime = models.DateTimeField(
        blank=True, null=True, verbose_name='保存时间')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Cargoin__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "goods": self.goods,
            "warehouse": self.warehouse,
            "amount": self.amount,
            "entrytime": self.entrytime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "staletime": self.staletime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'warehouse_cargoin'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'


class Cargoout(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='cargoout_by_goods')
    warehouse = models.ForeignKey(Warehouse, null=True, blank=True,
                                  on_delete=models.SET_NULL, related_name='cargoout_by_warehouse')
    order = models.ForeignKey(Order, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='cargoout_by_order')
    amount = models.IntegerField(blank=True, null=True, verbose_name='出货量')
    starttime = models.DateTimeField(
        blank=True, null=True, verbose_name='出库时间')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Cargoout__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "goods": self.goods,
            "warehouse": self.warehouse,
            "order": self.order,
            "amount": self.amount,
            "starttime": self.starttime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'warehouse_cargoout'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'
