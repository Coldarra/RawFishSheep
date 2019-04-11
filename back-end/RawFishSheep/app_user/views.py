from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

import sys
sys.path.append('../')

from decorator import *
from .models import *

@post
def test(request):
    return HttpResponse('OK')

@logout
@post
def log_in(request):

    context = {}
    print("LOGIN...")
    
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)

        inputinfo = {"username": username, "password": password}
        print("login", username, password)
        
        user = None
        try:  # 姓名登陆
            user = User.objects.get(username=username)
        except:
            pass
        try:  # 手机号登陆
            user = User.objects.get(phonenumber=username)
        except:
            pass
        try:  # 邮箱登陆
            user = User.objects.get(email=username)
        except:
            pass
        if user:  # 存在用户
            print(user)

            if check_password(password, user.password):
                print("验证成功")  # 比较成功，跳转index
                user.login(request)
                print(request.session['isLogin'])
                context = {'msg_code': 11000, 'msg': "登录成功", 'msg_type': "success",
                           'isLogin': True, 'username': True, 'password': True}
                return render(request, 'index.html', context)

            print("登录失败, 密码错误")  # 比较失败，还在login
            context = {'msg_code': 11002, 'msg': "密码错误，请重试。", 'msg_type': "danger", 'inputinfo': inputinfo,
                       'isLogin': False, 'username': True, 'password': False}
            return render(request, 'login.html', context)
        else:
            print("用户名不存在")  # 用户名不存在
            context = {'msg_code': 11001, 'msg': "用户不存在，请重试。", 'msg_type': "danger", 'inputinfo': inputinfo,
                       'isLogin': False, 'username': False}
            return render(request, 'login.html', context)

    print("表单获取失败")
    context = {'msg_code': 11003, 'msg': "表单获取失败，请重新登录。", 'msg_type': "danger", 'inputinfo': inputinfo,
               'isLogin': False, 'username': False}
    return render(request, 'login.html', context)

    # context = {'msg_code': 11010,
    #            'msg': "你进入到了异次元，请重新登录", 'isLogin': False}
    # return render(request, 'login.html', context)
