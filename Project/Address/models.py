from django.db import models

# Create your models here.
# Users用户关联
from Users.models import Users
from django.contrib.auth.models import User

# 收货地址Address
class Address(models.Model):
    # 地址编号
    id = models.AutoField(primary_key=True, verbose_name='地址编号')
    # 所属用户
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
    # 收货人姓名
    recv_name = models.CharField(max_length=255, verbose_name='收货人姓名')
    # 收货人联系方式
    recv_phone = models.CharField(max_length=50, verbose_name='收货人联系方式')
    # 国家
    native = models.CharField(max_length=255, verbose_name='国家')
    # 省区
    province = models.CharField(max_length=255, verbose_name='省区')
    # 市区
    city = models.CharField(max_length=255, verbose_name='市区')
    # 县区
    country = models.CharField(max_length=255, verbose_name='县区')
    # 街道
    street = models.CharField(max_length=255, verbose_name='街道')
    # 详细描述
    desc = models.CharField(max_length=255, verbose_name='详细描述')
    # 是否默认地址
    status = models.BooleanField(default=True,verbose_name='是否默认地址')
