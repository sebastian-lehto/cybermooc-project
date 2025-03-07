from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User

@login_required(login_url='profiles/login')
def index(request):

    users = User.objects.exclude(username="admin")
    context = {"users": users}
    
    return render(request, 'index.html', context)


def login(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    try:
        if User.objects.get(username=username).password == password:
            request.session['username'] = username
            return redirect('index')
        return redirect('loginView')
    except: 
        return redirect('loginView')
    
def logout(request):  
    del request.session['username']
    return redirect('loginView')

@login_required(login_url='profiles/login')
def profileView(request, uid):

    profile = User.objects.get(uid=uid)
    context = {"profile": profile}
    return render(request, 'profile.html', context)

def deleteView(request, uid):
    if request.user.is_superuser:
        User.objects.get(uid=uid).delete()

        users = User.objects.all()
        context = {"users": users}
    
def loginView(request):
    return render(request, 'registration/login.html')
