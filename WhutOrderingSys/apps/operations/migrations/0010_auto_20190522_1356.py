# Generated by Django 2.2 on 2019-05-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0009_auto_20190522_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='check_status',
            field=models.IntegerField(choices=[(0, '未提交'), (1, '提交审核'), (2, '已接单'), (3, '交易完成')], default=0, max_length=10, verbose_name='商家审核状态'),
        ),
    ]
