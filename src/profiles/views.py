from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User

def index(request):
    User.objects.all().delete()
    User.objects.create(username="Bob", uid=1).save()
    User.objects.create(username="Leah", uid=2).save()
    User.objects.create(username="Martin", uid=3).save()

    users = User.objects.all()
    context = {"users": users}
    return render(request, 'pages/index.html', context)

def profileView(request, uid):
    user = User.objects.get(uid=uid)
    context = {"user": user}
    return render(request, 'pages/profile.html', context)