from django.shortcuts import render, HttpResponse

# Create your views here.
from django.contrib.auth.views import login_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from Shopcart import models


# 下单
@login_required
@csrf_exempt
def create_shopcart_order(request):
    if request.method == 'GET':
        try:
            request.session['a'] = request.GET['all']
            request.session['b'] = request.GET['name']
            request.session['c'] = request.GET['num']
        except:
            pass
        return render(request, 'order/create_order.html')
    if request.method == 'POST':
        return HttpResponse('下单成功')