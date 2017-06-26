from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(req):
    logout(req)
    username = password = ''
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(req, user)
                return redirect('/person/main/')
        else:
            return redirect('/person/login_error/')
    else:
        return render(req, 'person/login.html', {
            'username': username, 'password': password
        })


def logout_user(req):
    logout(req)
    return render(req, 'person/logout.html')


def login_error(req):
    return render(req, 'person/login_error.html')


@login_required(login_url='/login/')
def main(req):
    user = req.user
    return render(req, 'person/main.html', {'user': user})
