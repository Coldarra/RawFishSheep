# Generated by Django 2.0.7 on 2019-05-08 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargoin',
            name='reason',
            field=models.CharField(default='default', max_length=20, verbose_name='入库原因'),
        ),
        migrations.AddField(
            model_name='cargoin',
            name='shelflife',
            field=models.IntegerField(blank=True, default=72, null=True, verbose_name='保质期'),
        ),
        migrations.AddField(
            model_name='cargoout',
            name='reason',
            field=models.CharField(default='default', max_length=20, verbose_name='出库原因'),
        ),
        migrations.AlterField(
            model_name='cargoin',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cargoin_by_goods', to='app_goods.Goods'),
        ),
        migrations.AlterField(
            model_name='cargoin',
            name='staletime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='过期时间'),
        ),
        migrations.AlterField(
            model_name='cargoin',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cargoin_by_warehouse', to='app_warehouse.Warehouse'),
        ),
        migrations.AlterField(
            model_name='cargoout',
            name='goods',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cargoout_by_goods', to='app_goods.Goods'),
        ),
        migrations.AlterField(
            model_name='cargoout',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cargoout_by_order', to='app_order.Order'),
        ),
        migrations.AlterField(
            model_name='cargoout',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cargoout_by_warehouse', to='app_warehouse.Warehouse'),
        ),
    ]