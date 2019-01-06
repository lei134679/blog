from django.shortcuts import render, redirect, reverse

# Create your views here.
from Goods.models import Goods
# 令牌
from django.views.decorators.csrf import csrf_exempt
# 登录验证
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import models


# 添加购物车
@login_required
def add_shopcart(request, id):
    try:
        models.Shopcart.objects.get(goods_id=int(id))
        return redirect(reverse('user:index'))
    except:
        a = Goods.objects.get(pk=int(id))
        # 购买数量：
        count = 1
        # 小计金额：
        subtotal = a.price
        models.Shopcart(count=count, subtotal=subtotal,goods_id=id, users_id=request.user.id).save()
        return redirect(reverse('user:index'))


# 列出所有
@login_required
def list_shopcart(request):
    list = models.Shopcart.objects.all()
    for i in list:
        print(i.goods.goodsimg_get.first.path)
    return render(request, 'shopcart/list_shopcart.html', {'list':list})


# 移除商品
@login_required
def del_shopcart(request, id):
    models.Shopcart.objects.filter(pk=id).delete()
    return redirect(reverse('shopcart:list_shopcart'))


@login_required
def shopcart(request):
    for i in request.user.shopcart_set.all():
        print(i.goods.goodsimage_set.all().first())
    return render(request, 'shopcart/shopcart.html', {})