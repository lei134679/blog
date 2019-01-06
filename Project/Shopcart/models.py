from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from Goods.models import Goods

# 购物车信息Shopcart
class Shopcart(models.Model):
    # 购物编号
    id = models.AutoField(primary_key=True, verbose_name='购物编号')
    # 购物商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='购物商品')
    # 购买数量
    count = models.IntegerField(verbose_name='购买数量')
    # 添加时间
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    # 小计金额
    subtotal = models.IntegerField(verbose_name='小计金额')
    # 所属用户
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')