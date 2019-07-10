# Generated by Django 2.2 on 2019-05-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0008_order_delivery_man'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='check_status',
            field=models.CharField(choices=[('0', '未提交'), ('1', '提交审核'), ('2', '已接单'), ('3', '交易完成')], default='0', max_length=10, verbose_name='商家审核状态'),
        ),
    ]