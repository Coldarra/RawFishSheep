# Generated by Django 2.0.7 on 2019-05-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='1', max_length=1, verbose_name='是否完成送货'),
        ),
    ]