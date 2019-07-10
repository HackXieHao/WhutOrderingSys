# Generated by Django 2.2 on 2019-05-11 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WindowInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window_no', models.CharField(max_length=11, verbose_name='窗口编号')),
                ('name', models.CharField(max_length=50, verbose_name='窗口名称')),
                ('love_num', models.IntegerField(verbose_name='收藏量')),
                ('desc', models.CharField(max_length=200, verbose_name='窗口描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '窗口信息',
                'verbose_name_plural': '窗口信息',
            },
        ),
    ]