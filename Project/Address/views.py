from django.shortcuts import render, redirect, reverse

# Create your views here.
from .models import Address
from django.http import HttpResponse, JsonResponse
# 令牌
from django.views.decorators.csrf import csrf_exempt
# 请求设置
from django.views.decorators.http import require_GET, require_POST ,require_safe, require_http_methods
# 登录验证
from  django.contrib.auth.decorators import login_required



# 新建地址
@login_required
@csrf_exempt
def found_address(request):
    if request.method == 'GET':
        return render(request, 'address/found.html')
    if request.method == 'POST':
        # 收货人姓名
        recv_name = request.POST.get('recv_name')
        # 收货人联系方式
        recv_phone = request.POST.get('recv_phone')
        # 国家
        native = request.POST.get('native')
        # 省区
        province = request.POST.get('province')
        # 市区
        city = request.POST.get('city')
        # 县区
        country = request.POST.get('country')
        # 街道
        street = request.POST.get('street')
        # 详细描述
        desc = request.POST.get('desc')
        # 是否默认地址
        status = request.POST.get('status')
        if status=='on':
            status=True
        elif status=='None':
            status=False
        a = Address(recv_name=recv_name, recv_phone=recv_phone, native=native, province=province, city=city,
                country=country, street=street, desc=desc, status=status, users_id=request.user.id)
        a.save()
        return render(request, 'index1.html')


# 列出所有地址
@login_required
def list_address(request):
    addr = Address.objects.all()
    return render(request, 'address/list_address.html', {'add': addr})


# 修改地址
@login_required
@csrf_exempt
def revise_address(request, id):
    if request.method == 'GET':
        addr = Address.objects.get(pk=id)
        return render(request, 'address/revise_address.html', {"addr":addr})
    if request.method == 'POST':
        # 收货人姓名
        recv_name = request.POST.get('recv_name')
        # 收货人联系方式
        recv_phone = request.POST.get('recv_phone')
        # 国家
        native = request.POST.get('native')
        # 省区
        province = request.POST.get('province')
        # 市区
        city = request.POST.get('city')
        # 县区
        country = request.POST.get('country')
        # 街道
        street = request.POST.get('street')
        # 详细描述
        desc = request.POST.get('desc')
        # 是否默认地址
        status = request.POST.get('status')
        if status=='on':
            status=True
        elif status=='None':
            status=False
        Address.objects.filter(pk=id).update(recv_name=recv_name, recv_phone=recv_phone, native=native, province=province, city=city,
                country=country, street=street, desc=desc, status=status, users_id=request.user.id)
        return render(request, 'index1.html')


# 删除地址
def del_address(request, id):
    Address.objects.filter(pk=id).delete()
    return redirect(reverse('address:list_address'))





