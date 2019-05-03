from django.db import models
import pytz

tz = pytz.timezone('Asia/Shanghai')


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    gender = models.CharField(blank=True, null=True,
                              max_length=30, verbose_name='性别')
    phonenumber = models.CharField(
        max_length=30, unique=True, verbose_name='手机号')
    email = models.CharField(blank=True, null=True,
                             max_length=50, verbose_name='邮箱')
    level = models.CharField(
        default='user', max_length=20, verbose_name='用户等级')
    about = models.CharField(blank=True, null=True,
                             max_length=200, verbose_name='关于')
    headid = models.IntegerField(
        default=0, blank=True, null=True, verbose_name='头像')
    registertime = models.DateTimeField(verbose_name='注册时间')
    isdelete = models.CharField(default='0', max_length=1, verbose_name='是否删除')

    def login(self, request):
        request.session.flush()
        request.session['isLogin'] = True
        request.session['username'] = self.username
        request.session['userid'] = self.id
        request.session['headid'] = self.headid
        request.session['level'] = self.level

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "gender": self.gender,
            "phonenumber": self.phonenumber,
            "email": self.email,
            "level": self.level,
            "about": self.about,
            "headid": self.headid,
            "registertime": self.registertime.astimezone(tz).strftime("%Y/%m/%d %H:%M:%S"),
        }

    def toDelete(self):
        self.isdelete = '1'
        self.save()
        return True

    def __str__(self):
        text = "__User__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    class Meta:
        db_table = 'user_info'
        verbose_name = 'RawFishSheep'
        app_label = 'app_user'


class Address(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='address_by_user')
    name = models.CharField(
        max_length=50, default="receiver", verbose_name='收货人')
    phonenumber = models.CharField(
        max_length=30, default="phonenumber", verbose_name='手机号')
    address = models.CharField(
        max_length=100, default="address", verbose_name='详细地址')
    status = models.CharField(default='1', max_length=1, verbose_name='地址状态')
    # status d:已删除 1:正常 0:默认值

    def __str__(self):
        text = "__Address__\n"
        for key, value in self.toDict().items():
            text += "{}: {}\n".format(key, value)
        return text

    def toDict(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "name": self.name,
            "phonenumber": delf.phonenumber,
            "address": self.address,
            "status": self.status,
        }

    def toDelete(self):
        self.status = 'd'
        self.save()
        return True

    class Meta:
        db_table = 'user_address'
        verbose_name = 'RawFishSheep'
        app_label = 'app_user'
