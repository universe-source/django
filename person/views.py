from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(req):
    logout(req)
    username = password = ''
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect('/main/')

    return render(req, 'person/login.html', {
        'username': username, 'password': password
    })


@login_required(login_url='/login/')
def main(req):
    user = req.user
    return render_to_response('person/main.html', {'user': user})
