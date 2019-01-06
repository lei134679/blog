from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# 店铺信息
class Store(models.Model):
    # 店铺编号
    id = models.AutoField(primary_key=True, verbose_name='店铺编号')
    # 店铺名称
    name = models.CharField(max_length=255, verbose_name='店铺名称')
    # 店铺封面
    cover = models.ImageField(upload_to='static/images/Store/',
                              default='static/images/Store/default.jpg'
                              , verbose_name='店铺封面')
    # 店铺描述：
    intro = HTMLField(verbose_name='店铺描述')
    # 开店时间
    opener_time = models.DateTimeField(auto_now_add=True, verbose_name='开店时间')
    # 店铺状态
    status = models.BooleanField(default=True, verbose_name='店铺状态')
    # 所属用户
    users = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')