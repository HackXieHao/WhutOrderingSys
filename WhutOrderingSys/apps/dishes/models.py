from django.db import models
from datetime import datetime
from orderWindows.models import WindowInfo

# Create your models here.
class DishInfo(models.Model):
    image = models.ImageField(upload_to='books/', verbose_name='菜品图片')
    dish_no = models.CharField(max_length=11, verbose_name='菜品编号')
    name = models.CharField(max_length=200, verbose_name='菜品名称')
    price = models.FloatField(verbose_name='价格')
    order_num = models.IntegerField(verbose_name='订购数量')
    love_num = models.IntegerField(verbose_name='收藏量')
    window = models.ForeignKey(WindowInfo, verbose_name='所属窗口', on_delete=models.CASCADE)
    desc = models.CharField(max_length=200, verbose_name='菜品描述')
    detail = models.CharField(max_length=1000, verbose_name='菜品详情')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜品信息'
        verbose_name_plural = verbose_name