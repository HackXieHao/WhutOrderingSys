from django.db import models
from datetime import datetime

# Create your models here.
class WindowType(models.Model):
    name = models.CharField(max_length=50, verbose_name='类型名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '窗口类别信息'
        verbose_name_plural = verbose_name

class WindowInfo(models.Model):
    image = models.ImageField(verbose_name='窗口图片')
    window_no = models.CharField(max_length=11, verbose_name='窗口编号')
    window_type = models.ForeignKey(WindowType, verbose_name='窗口类别', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='窗口名称')
    love_num = models.IntegerField(verbose_name='收藏量')
    desc = models.CharField(max_length=200, verbose_name='窗口描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '窗口信息'
        verbose_name_plural = verbose_name

