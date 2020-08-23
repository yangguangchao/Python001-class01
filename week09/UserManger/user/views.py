from django.shortcuts import render,redirect
from .form import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import logging

def index(request):
    name = request.user.username
    return render(request, 'index.html', {'name':name})

def login_user(request):
    try:
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                # 读取表单的返回值
                cd = login_form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                print(user)
                if user:
                    # 登陆用户
                    login(request, user)
                    # 登录成功，返回到首页
                    return redirect(index)
                else:
                    return HttpResponse('登录失败,密码错误')
            else:
                return HttpResponse('请使用post方法请求')
        # GET
        if request.method == "GET":
            login_form = LoginForm()
            return render(request, 'form.html', {'form': login_form})
    except Exception as e:
        logging.error(e)
        print(e)
    return render(request, 'form.html', {'form': login_form})
