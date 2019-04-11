from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    gender = models.CharField(max_length=30, verbose_name='性别')
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

    def login(request):
        request.session['isLogin'] = True
        request.session['username'] = self.username
        request.session['userid'] = self.id
        request.session['headid'] = self.headid
        request.session['level'] = self.level

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
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
        text = ""
        for key, value in self.toDict():
            text += "{}: {}/n".format(key, value)
        return text

    class Meta:
        db_table = 'userinfo'
        verbose_name = 'RawFishSheep'
        app_label = 'app_user'
