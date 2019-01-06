from django.db import models

# Create your models here.
from tinymce.models import HTMLField


# 商品类型GoodsType
class GoodsType(models.Model):
    # 类型主键
    id = models.AutoField(primary_key=True, verbose_name='类型主键')
    # 类型名称
    gt_name = models.CharField(max_length=255, verbose_name='类型名称')
    # 图片
    cover = models.ImageField(upload_to='static/images/GoodsType/',null=True, blank=True,
                              verbose_name='图片')
    # 类型描述
    gt_desc = HTMLField(max_length=255, verbose_name='类型描述')
    # 父级类型：
    null = models.ForeignKey('self', null=True)