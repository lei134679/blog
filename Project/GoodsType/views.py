from django.shortcuts import render, HttpResponse, redirect
# 令牌
from django.views.decorators.csrf import csrf_exempt
# 登录验证
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models


# 设置类型
@login_required
@csrf_exempt
def set_goodstype(request):
    if request.method == 'GET':
        return render(request, 'goodstype/set_goodstype.html')
    if request.method == 'POST':
        # 类型名称：
        gt_name = request.POST['gt_name']
        # 图片：
        cover = request.FILES['cover']
        # 类型描述：
        gt_desc = request.POST['gt_desc']
        # print(gt_name, cover, gt_desc)
        models.GoodsType(gt_name=gt_name, cover=cover, gt_desc=gt_desc).save()
        return render(request, 'index1.html')


# 列出所有类型
def list_goodstype(request):
    list = models.GoodsType.objects.all()
    return render(request, 'goodstype/list_goodstype.html', {'list': list})


# 修改类型
@login_required
@csrf_exempt
def revise_goodstype(request, id):
    if request.method == 'GET':
        revise = models.GoodsType.objects.get(id=id)
        return render(request, 'goodstype/revise_goodstype.html', {'id':id, 'revise': revise})
    if request.method == 'POST':
        # 类型名称：
        gt_name = request.POST['gt_name']
        # 图片：
        cover = request.FILES['cover']
        # 类型描述：
        gt_desc = request.POST['gt_desc']
        models.GoodsType.objects.filter(id=id).update(gt_name=gt_name, cover=cover, gt_desc=gt_desc)
        return redirect('goodstype:list_goodstype')


# 删除类型
def del_goodstype(request, id):
    models.GoodsType.objects.get(id=id).delete()
    return redirect('goodstype:list_goodstype')

