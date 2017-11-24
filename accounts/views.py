# coding:utf8
#  from smtplib import SMTPException
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import LoginForm


def home(req):
    """模板使用方法见:
    http://python.usyiyi.cn/documents/django_182/ref/templates/upgrading.html
    """
    if req.user.is_active:
        pass
    else:
        pass
    return render(req, 'index.html')


def about(req):
    return render(req, 'about.html')


@login_required(login_url='/accounts/login/')
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
                    return redirect('/')
            else:
                message = 'Invalid username/password.'
    else:
        form = LoginForm()
    return render(req, 'accounts/login.html', {
        'message': message, 'form': form})


@login_required(login_url='/accounts/login/')
def logout_user(req):
    logout(req)
    return render(req, 'accounts/logout.html')


def login_error(req):
    return render(req, 'accounts/login_error.html')
