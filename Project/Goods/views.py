from django.shortcuts import render, redirect, reverse

# Create your views here.
# 令牌
from django.views.decorators.csrf import csrf_exempt
# 登录验证
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import models
from GoodsImage.models import GoodsImage


# 添加商品
@login_required
@csrf_exempt
def add_goods(request):
    if request.method == 'GET':
        GoodsType = models.GoodsType.objects.all()
        store = models.Store.objects.all()
        return render(request, 'goods/add_goods.html', {'GoodsType':GoodsType, 'store':store})
    if request.method == 'POST':
        # 商品名称：
        name = request.POST['name']
        # 商品单价：
        price = request.POST['price']
        # 商品库存：
        stock = request.POST['stock']
        # 销售数量：
        count = request.POST['count']
        # 商品介绍：
        desc = request.POST['desc']
        # 所属类型
        goodstype = request.POST['goodstype']
        # 所属店铺
        store = request.POST['store']
        # 获得对应类型id
        gt = models.GoodsType.objects.get(gt_name=goodstype)
        # 获取对应商店id
        st = models.Store.objects.get(name=store)
        result = models.Goods(name=name, price=price, stock=stock, count=count, desc=desc, goods_detail_type_id=gt.id, goods_store_id=st.id)
        result.save()
        return redirect(reverse('store:list_store'))


# 列出商品
@login_required
def list_goods(request):
    list = models.Goods.objects.all()
    img = GoodsImage.objects.all()
    return render(request, 'goods/list_goods.html', {'list':list, 'img':img})


# 修改商品
@login_required
@csrf_exempt
def revise_goods(request, id):
    if request.method == 'GET':
        goods = models.Goods.objects.get(id=id)
        GoodsType = models.GoodsType.objects.all()
        store = models.Store.objects.all()
        return render(request, 'goods/revise_goods.html', {'GoodsType':GoodsType, 'store':store, 'goods':goods})
    if request.method == 'POST':
        # 商品名称：
        name = request.POST['name']
        # 商品单价：
        price = request.POST['price']
        # 商品库存：
        stock = request.POST['stock']
        # 销售数量：
        count = request.POST['count']
        # 商品介绍：
        desc = request.POST['desc']
        # 所属类型
        goodstype = request.POST['goodstype']
        # 所属店铺
        store = request.POST['store']
        # 获得对应类型id
        gt = models.GoodsType.objects.get(gt_name=goodstype)
        # 获取对应商店id
        st = models.Store.objects.get(name=store)
        models.Goods.objects.filter(id=id).update(name=name, price=price, stock=stock, count=count, desc=desc, goods_detail_type_id=gt.id, goods_store_id=st.id)
        return redirect('goods:list_goods')


# 删除商品
@login_required
def del_goods(request, id):
    models.Goods.objects.filter(id=id).delete()
    return redirect('goods:list_goods')


# 商品详情
def details_goods(request):
    list = models.Goods.objects.all()
    return render(request, 'goods/details_goods.html', {'list':list})