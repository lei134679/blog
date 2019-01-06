from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# 令牌
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import models

# 注册店铺
@login_required
@csrf_exempt
def set_store(request):
    if request.method == 'GET':
        return render(request, 'store/shop_store.html')
    if request.method == 'POST':
        try:
            # 获得页面信息
            # 店铺名称：
            name = request.POST.get('name')
            # 店铺封面：
            cover = request.FILES.get('cover')
            # 店铺描述：
            intro = request.POST.get('intro')
            # 店铺状态：
            status = request.POST.get('status')
            if status=='on':
                status=True
            elif status==None:
                status=False
            print(request.user.id)
            store = models.Store(name=name, cover=cover, status=status,intro=intro, users_id=request.user.id)
            store.save()
            return render(request, 'index1.html')
        except:
            return render(request, 'store/shop_store.html', {'str': '输入有误'})


# 列出所有店铺
@csrf_exempt
@login_required
def list_store(request):
    result = models.Store.objects.filter(users_id=request.user.id)
    for i in result:
        for j in i.goods_set.all():
            for img in j.goodsimage_set.all():
                print(img.path)
    return render(request, 'store/list_store.html', {'result': result})


# 删除店铺
@csrf_exempt
@login_required
def del_store(request, id):
    result = models.Store.objects.filter(id=id)
    result.delete()
    return redirect('store:list_store')


# 修改店铺
@csrf_exempt
@login_required
def revise_store(request, id):
    if request.method == 'GET':
        store = models.Store.objects.all().get(id=id)
        return render(request, 'store/revise_store.html', {'id':id, 'store': store})
    if request.method == 'POST':
        try:
            # 获得页面信息
            # 店铺名称：
            name = request.POST.get('name')
            # 店铺封面：
            cover = request.FILES.get('cover')
            # 店铺描述：
            intro = request.POST.get('intro')
            # 店铺状态：
            status = request.POST.get('status')
            if status == 'on':
                status = True
            elif status == None:
                status = False
            print(request.user.id)
            models.Store.objects.filter(id=id).update(name=name, cover=cover, intro=intro, status=status)
            return render(request, 'index1.html')
        except:
            return render(request, 'store/shop_store.html', {'str': '输入有误'})


