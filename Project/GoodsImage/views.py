from django.shortcuts import render, redirect, reverse

# Create your views here.
from . import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# 添加图片
@login_required
@csrf_exempt
def add_goodsimage(request, id):
    if request.method == 'GET':
        return render(request, 'goodsimage/add_goodsimage.html', {'id':id})
    if request.method == 'POST':
        # 图片路径：
        path = request.FILES['path']
        # 默认展示：
        status = request.POST['status']
        if status == 'on':
            status = True
        elif status == 'None':
            status = False
        models.GoodsImage(path=path, status=status, goods_id=id).save()
        return redirect(reverse('store:list_store'))


# 删除图片
def del_goodsimage(request, id):
    models.GoodsImage.objects.filter(id=id).delete()
    return redirect(reverse('store:list_store'))