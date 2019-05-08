from django.db import models
from app_user.models import *
from app_order.models import *
from app_goods.models import *

# Create your models here.


class Warehouse(models.Model):
    # name = models.CharField(max_length=30, verbose_name='仓库名称')
    address = models.CharField(max_length=300, verbose_name='仓库地址')

    def __str__(self):
        text = "__Warehouse__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "address": self.address,
        }

    def toDelete(self):
        self.delete()
        return

    class Meta:
        db_table = 'warehouse'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'


class Cargoin(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='cargoin_by_goods')
    warehouse = models.ForeignKey(Warehouse, null=True, blank=True,
                                  on_delete=models.DO_NOTHING, related_name='cargoin_by_warehouse')
    amount = models.IntegerField(blank=True, null=True, verbose_name='进货量')
    cost = models.IntegerField(
        blank=True, null=True, verbose_name='进货成本')  # 单位: 分
    entrytime = models.DateTimeField(
        blank=True, null=True, verbose_name='入库时间')
    shelflife = models.IntegerField(
        blank=True, null=True, default=72, verbose_name='保质期')  # 单位: 小时
    staletime = models.DateTimeField(
        blank=True, null=True, verbose_name='过期时间')
    reason = models.CharField(
        default='default', max_length=20, verbose_name='入库原因')
    # 默认: 'default'  商品退货: 'refund'
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
            "goods": self.goods.name,
            "warehouse": self.warehouse.address,
            "amount": self.amount,
            "entrytime": self.entrytime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "shelflife": self.shelflife,
            "staletime": self.staletime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "reason": self.reason,
            "isdelete": self.isdelete,
            "cost": self.cost,
        }

    class Meta:
        db_table = 'warehouse_cargoin'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'


class Cargoout(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='cargoout_by_goods')
    warehouse = models.ForeignKey(Warehouse, null=True, blank=True,
                                  on_delete=models.DO_NOTHING, related_name='cargoout_by_warehouse')
    order = models.ForeignKey(Order, null=True, blank=True,
                              on_delete=models.DO_NOTHING, related_name='cargoout_by_order')
    reason = models.CharField(
        default='default', max_length=20, verbose_name='出库原因')
    # 默认: 'default'  商品返厂: 'refund'  商品下架: offshelves
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
            "reason": self.reason,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'warehouse_cargoout'
        verbose_name = 'RawFishSheep'
        app_label = 'app_warehouse'
