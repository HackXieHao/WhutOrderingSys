# Generated by Django 2.2 on 2019-05-22 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_deliveryman'),
        ('operations', '0007_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_man',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.DeliveryMan', verbose_name='快递员号'),
            preserve_default=False,
        ),
    ]
