from django.db import models

# Create your models here.
from Goods.models import Goods


# 商品图片GoodsImage
class GoodsImage(models.Model):
    # 图片编号
    id = models.AutoField(primary_key=True, verbose_name='图片编号')
    # 图片路径
    path = models.ImageField(upload_to='static/images/GoodsImage/',
                             null=True, blank=True, verbose_name='图片路径')
    # 默认展示
    status = models.BooleanField(default=True, verbose_name='默认展示')
    # 所属商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='所属商品')