from django.shortcuts import render, HttpResponse, redirect, reverse

# Create your views here.
# 令牌
from django.views.decorators.csrf import csrf_exempt
# 模块
from . import models
# 外键
from django.contrib.auth import login, authenticate, logout
# 登录验证
from django.contrib.auth.decorators import login_required
from GoodsType.models import GoodsType
from Goods.models import Goods
import random
import urllib
import http
# 验证码
from django.http import JsonResponse
host = "106.ihuyi.com"  #ip（域名）
sms_send_uri = "/webservice/sms.php?method=Submit"  # pyhton短信接口
account = "C63991011" # APIID
password = "4ecfac486249d5dd8ed8afd295f66698"  # APIKEY


# 首页
def index(request):
    # 一级类型
    all = GoodsType.objects.filter(null__isnull=True)
    goods = Goods.objects.all()
    img = []
    for i in goods:
        for j in i.goodsimage_set.all():
            img.append(j.path)
    try:
        return render(request, 'index1.html', {'all': all, 'goods': goods, 'img': img[0]})
    except:
        return render(request, 'index1.html', {'all': all, 'goods': goods})


# 注册
@csrf_exempt
def regist_user(request):
    if request.method == 'GET':
        return render(request, 'user/regist.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST.get('username')    # 登录账号
        userpass = request.POST.get('userpass')      # 登录密码
        mickname = request.POST.get('nickname')    # 用户昵称
        age = request.POST.get('age')     # 用户年龄
        gender = request.POST.get('gender')  # 用户性别
        header = request.FILES.get('header')  # 用户头像
        phone = request.POST.get('phone')   # 联系方式
        email = request.POST.get('email')  # 电子邮箱
        try:
            # 判断账号
            if len(username) < 6 or len(username) > 18:
                return render(request, 'user/regist.html', {'username': '账号6-18位'})
            # 判断密码
            if len(userpass) < 6 or len(userpass) > 18:
                return render(request, 'user/regist.html', {'userpass': '密码6-18位'})
            # 判断昵称
            if ' ' in mickname:
                return render(request, 'user/regist.html', {'nickname': '昵称不包含空格'})
            # 判断年龄
            if age < str(0) or age > str(200):
                return render(request, 'user/regist.html', {'age': '年龄输入有误'})
            # 保存数据库
            auth_user = models.User.objects.create_user(username=username, password=userpass, email=email)
            auth_user.save()
            # 保存数据库
            user = models.Users(mickname=mickname, age=age, gender=gender, feader=header, phone=phone,
                                user=auth_user)
            user.save()
            return render(request,'index1.html')
        except:return render(request, 'user/regist.html', {'str': '输入有误'})


# 登录
@csrf_exempt
def login_user(request):
    if request.method == 'GET':
        # 获得地址
        next_url = request.GET.get("next")
        # 放入会话
        request.session['next_url']=next_url
        return render(request, 'user/login_user.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST.get('username')  # 登录账号
        userpass = request.POST.get('userpass')  # 登录密码
        user = authenticate(username=username, password=userpass)  # 验证:返回验证对象,失败则是None
        if user:
            login(request, user)
            # 获得会话信息
            next_url = request.session.get('next_url')
            if next_url is None:
                return redirect(index)
            return redirect(next_url)
        else:
            error = "账号或者密码错误"
            return render(request, "user/login_user.html", {'error': error})


# 登出
def logout_user(request):
    logout(request)
    request.session.clear()
    return redirect("/user/index")


# 修改资料
@login_required
@csrf_exempt
def data_user(request):
    if request.method == 'GET':
        return render(request, 'user/data_user.html')
    if request.method == 'POST':
        # 获得页面信息
        mickname = request.POST.get('nickname')    # 用户昵称
        age = request.POST.get('age')     # 用户年龄
        gender = request.POST.get('gender')  # 用户性别
        header = request.FILES.get('header')  # 用户头像
        phone = request.POST.get('phone')   # 联系方式
        email = request.POST.get('email')  # 电子邮箱
        try:
            # 判断昵称
            if ' ' in mickname:
                return render(request, 'user/data_user.html', {'nickname': '昵称不包含空格'})
            # 判断年龄
            if age < str(0) or age > str(200):
                return render(request, 'user/data_user.html', {'age': '年龄输入有误'})
            # 保存数据库
            models.User.objects.filter(id=request.user.id).update(email=email)
            # 保存数据库
            auth_user = models.User.objects.get(id=request.user.id)
            models.Users.objects.filter(user_id=request.user.id).update(mickname=mickname, age=age, gender=gender,
                                                                        feader=header, phone=phone, user=auth_user)
        except:return render(request, 'user/data_user.html', {'str': '输入有误'})
        return redirect(reverse('user:index'))


# 修改密码
@login_required
@csrf_exempt
def data_pwd(request):
    if request.method == 'GET':
        return render(request, 'user/data_pwd.html')
    if request.method == 'POST':
        # 获得页面信息
        username = request.POST.get('username')  # 登录账号
        userpass = request.POST.get('userpass')  # 登录密码
        models.User.objects.filter(id=request.user.id).update(username=username, password=userpass)
        logout(request)
        return render(request, "user/login_user.html", {'str':'修改密码成功，请重新登录'})


# 个人资料
@login_required
def data_data(request):
    print(request.user.address_set)
    return render(request, 'user/data_data.html')


# 关于我们
@login_required
def about(request):
    return render(request, 'user/about.html')


def send_message(request):
    """发送手机验证码"""
    # 获取ajax的get方法发送过来的手机号码
    tel = request.GET.get('tel')
    # 通过手机去查找用户是否已经注册
    user = models.Users.objects.filter(tel=tel)
    if len(user) == 1:
        return JsonResponse({'msg': "该手机已经注册"})
    # 定义一个字符串,存储生成的6位数验证码
    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    # 拼接成发出的短信
	# 这是平台的默认模板，想改模板要收费且贵的很，要一字不差的写
	# 您的验证码是：【变量】。请不要把验证码泄露给其他人。
	# 请将【变量】替换成需要发送的内容，平台将使用您的账号发送此模板到您指定的手机上
    text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
    # 把请求参数编码
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': tel, 'format': 'json'})
    # 请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 通过全局的host去连接服务器
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 得到服务器的响应
    response = conn.getresponse()
    # 获取响应的数据
    response_str = response.read()
    # 关闭连接
    conn.close()
    print('-----', text)
    print('-----', tel)
    print('-----', message_code)
    # 把验证码放进session中
    request.session['message_code'] = message_code
    print(eval(response_str.decode()))
    # 使用eval把字符串转为json数据返回
    return JsonResponse(eval(response_str.decode()))