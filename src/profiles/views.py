from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import User

def index(request):
    if not request.session.get('username'): return redirect(loginView)

    users = User.objects.exclude(username="admin")
    context = {"users": users}
    
    return render(request, 'pages/index.html', context)


@csrf_exempt
def login(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    try:
        # Fix: A more secure authentication method with the Django authenitcation system
        # user = authenticate(request, username=username, password=password)
        if User.objects.get(username=username).password == password:
            request.session['username'] = username
            return redirect('index')
        return redirect('loginView')
    except: 
        return redirect('loginView')
    
def infoView(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'info.html', context)

def logout(request):  
    del request.session['username']
    return redirect('loginView')

def profileView(request, uid):
    user = User.objects.get(uid=uid)
    context = {"user": user}
    return render(request, 'pages/profile.html', context)

def deleteView(request, uid):
    # @staff_member_required       or
    # user.has_perm("myapp.delete_users")

    User.objects.get(uid=uid).delete()

    users = User.objects.all()
    context = {"users": users}
    
def loginView(request):
    setUp()
    return render(request, 'pages/login.html')

def setUp():
    User.objects.all().delete()
    User.objects.update_or_create(username="Bob", uid=1, password="1234", email="bob@mail.com")[0].save()
    User.objects.update_or_create(username="Leah", uid=2, password="1234", email="leah@mail.com")[0].save()
    User.objects.update_or_create(username="Martin", uid=3, password="1234", email="martin@mail.com")[0].save()
    User.objects.update_or_create(username="admin", uid=0, password="12345", email="admin@mail.com")[0].save()