from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# 用户类Users
class Users(models.Model):
    # 用户编号
    id = models.AutoField(primary_key=True, verbose_name='用户编号')
    # 用户昵称
    mickname = models.CharField(max_length=255, unique=True, verbose_name='用户昵称')
    # 用户年龄
    age = models.CharField(max_length=200, verbose_name='用户年龄')
    # 用户性别
    gender = models.CharField(max_length=50, verbose_name='用户性别')
    # 用户头像
    feader = models.ImageField(upload_to='static/images/User_header/',
                               default='static/images/User_header/default.jpg'
                               , verbose_name='用户头像')
    # 联系方式
    phone = models.CharField(max_length=50, verbose_name='联系方式')
    # 和auth_user关联
    user = models.OneToOneField(User, on_delete=models.Model, verbose_name='关联')
