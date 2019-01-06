from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# 订单Order
class Order(models.Model):
    # 订单编号
    id = models.AutoField(primary_key=True, verbose_name='订单编号')
    # 下单时间
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    # 所属用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
    # 收货人
    users = models.CharField(max_length=255, verbose_name='收货人')
    # 收货地址
    recv_address = models.CharField(max_length=255, verbose_name='收货地址')
    # 联系方式
    recv_phone = models.CharField(max_length=50, verbose_name='联系方式')
    # 总计金额
    totale = models.IntegerField(verbose_name='总计金额')