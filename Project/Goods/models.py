from django.db import models

# Create your models here.
from GoodsType.models import GoodsType
from Store.models import Store
from tinymce.models import HTMLField


# 商品信息Goods
class Goods(models.Model):
    # 商品编号
    id = models.AutoField(primary_key=True, verbose_name='商品编号')
    # 商品名称
    name = models.CharField(max_length=255, verbose_name='商品名称')
    # 商品单价
    price = models.IntegerField(verbose_name='商品单价')
    # 商品库存
    stock = models.IntegerField(verbose_name='商品库存')
    # 销售数量
    count = models.IntegerField(verbose_name='销售数量')
    # 上架时间
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上架时间')
    # 商品介绍
    desc = HTMLField(verbose_name='商品介绍')
    # 商品类型
    goods_detail_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE,
                                          verbose_name='商品类型')
    # 所属店铺
    goods_store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='所属店铺')

