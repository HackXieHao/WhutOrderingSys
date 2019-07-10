from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from orderWindows.models import WindowInfo

# Create your models here.
class UserInfo(AbstractUser):
    image = models.ImageField(upload_to='user/', verbose_name='用户头像', null=True, blank=True)
    name = models.CharField(verbose_name='用户姓名', max_length=20)
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), verbose_name='性别', default='girl', max_length=10)
    phone = models.CharField(max_length=11, verbose_name='手机号', null=True, blank=True)
    student_code = models.CharField(max_length=11, verbose_name='学号')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='地址')
    # type = models.CharField(choices=((1, '管理员'), (2, '学生')), verbose_name='用户类型', max_length=10)
    is_start = models.BooleanField(default=False, verbose_name='是否激活')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class DeliveryMan(models.Model):
    name = models.CharField(max_length=10, verbose_name='快递员姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    manage_window = models.ForeignKey(WindowInfo, verbose_name='配送窗口', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = '快递员信息'
        verbose_name_plural = verbose_name