# Generated by Django 2.0.7 on 2019-05-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0005_auto_20190508_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='price',
            field=models.IntegerField(default=0, verbose_name='单价'),
        ),
    ]