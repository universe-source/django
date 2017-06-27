# coding:utf8
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from smtplib import SMTPException
from .models import LoginForm


def home(req):
    if req.user.is_active:
        pass
    else:
        pass
    return render(req, 'index.html')

    
def about(req):
    return render(req, 'about.html')


def contact(req):
    errors = []
    # 注意，测试时不要添加test等字段
    if req.method == 'POST':
        if not req.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not req.POST.get('message', ''):
            errors.append('Enter a message.')
        if req.POST.get('email') and '@' not in req.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            recipient_list = [req.POST.get('email')]
            print recipient_list
            send_mail(
                subject=req.POST['subject'],
                message=req.POST['message'],
                from_email='ilifediary2@163.com', 
                recipient_list=recipient_list,
                fail_silently=False
            )
            return redirect('/thanks/')
    return render(req, 'contact.html', {'errors': errors})


def thanks(req):
    return render(req, 'thanks.html')


# Create your views here.
def login_user(req):
    message = None
    if req.POST:
        # 使用表单类
        form = LoginForm(req.POST)
        if form.is_valid():
            username = req.POST['username']
            password = req.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return redirect('/person/main/')
            else:
                message = 'Invalid username/password.'
    else:
        form = LoginForm()
    return render(req, 'person/login.html', {
        'message': message, 'form': form
        })


@login_required(login_url='/person/login/')
def logout_user(req):
    logout(req)
    return render(req, 'person/logout.html')


def login_error(req):
    return render(req, 'person/login_error.html')


# 如果没有登录，则直接跳转到登录界面
@login_required(login_url='/person/login/')
def main(req):
    user = req.user
    return render(req, 'person/main.html', {'user': user})
