# Generated by Django 2.2 on 2019-05-24 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderWindows', '0003_auto_20190512_2339'),
        ('operations', '0011_auto_20190522_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_window',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orderWindows.WindowInfo', verbose_name='所属窗口'),
            preserve_default=False,
        ),
    ]
