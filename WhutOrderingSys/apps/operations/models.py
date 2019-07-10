from django.db import models
from dishes.models import DishInfo
from users.models import UserInfo
from orderWindows.models import WindowInfo
from datetime import datetime
from users.models import DeliveryMan

# Create your models here.
# 订单信息
class Order(models.Model):
    order_no = models.CharField(max_length=11, verbose_name='订单编号')
    dish_id = models.ForeignKey(DishInfo, verbose_name='菜品号', on_delete=models.CASCADE)
    order_window = models.ForeignKey(WindowInfo, verbose_name='所属窗口', on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, verbose_name='用户号', on_delete=models.CASCADE)
    order_status = models.BooleanField(verbose_name='订购状态')
    number = models.IntegerField(verbose_name='订购数量')
    desc = models.CharField(max_length=200, verbose_name='备注')
    check_status = models.IntegerField(choices=((0, '未提交'), (1, '提交审核'),(2, '已接单'),(3, '交易完成')), verbose_name='商家审核状态', default=0)
    delivery_man = models.ForeignKey(DeliveryMan, verbose_name='快递员号', on_delete= models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.order_no

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

# 收藏信息
class Love(models.Model):
    user_id = models.ForeignKey(UserInfo, verbose_name='用户号', on_delete=models.CASCADE)
    love_id = models.IntegerField(verbose_name='收藏id')
    love_type = models.CharField(choices=((1, 'dish'), (2, 'window')), verbose_name='收藏类别', max_length=10)
    love_status = models.BooleanField(default=False, verbose_name='收藏状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.love_student.name

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name

