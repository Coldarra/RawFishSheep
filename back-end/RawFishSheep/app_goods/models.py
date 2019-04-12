from django.db import models

# Create your models here.


class Category(models.Model):
    superior = models.IntegerField(
        null=True, blank=True, default=0, verbose_name='上级分类')
    name = models.CharField(max_length=50, verbose_name='类别名')
    level = models.IntegerField(
        default=1, blank=True, null=True, verbose_name='等级')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Category__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "superior": self.superior,
            "name": self.name,
            "level": self.level,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'goods_category'
        verbose_name = 'RawFishSheep'
        app_label = 'app_goods'


class Goods(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name='goods_by_Category')
    name = models.CharField(max_length=100, verbose_name='商品名称')
    unit = models.CharField(default='ge', max_length=10, verbose_name='商品单位')
    status = models.CharField(max_length=1, verbose_name='商品状态')
    price = models.IntegerField(
        default=-1, blank=True, null=True, verbose_name='当前价格')
    remain = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='余量')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Goods__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "category": self.category.name,
            "name": self.name,
            "unit": self.unit,
            "status": self.status,
            "price": self.price,
            "remain": self.remain,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'goods'
        verbose_name = 'RawFishSheep'
        app_label = 'app_goods'


class Picture(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='picture_by_goods')
    path = models.CharField(max_length=100, verbose_name='图片地址')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__Picture__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "goods": self.goods.name,
            "path": self.path,
            "isdelete": self.isdelete,
        }

    class Meta:
        db_table = 'goods_picture'
        verbose_name = 'RawFishSheep'
        app_label = 'app_goods'


class History(models.Model):
    goods = models.ForeignKey(Goods, null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='history_by_goods')
    updatetime = models.DateTimeField(
        blank=True, null=True, verbose_name='定价时间')
    price = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='定价')

    def __str__(self):
        text = "__History__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "goods": self.goods.name,
            "updatetime": self.updatetime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
            "price": self.price,
        }

    class Meta:
        db_table = 'goods_history'
        verbose_name = 'RawFishSheep'
        app_label = 'app_goods'
