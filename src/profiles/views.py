from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User

def index(request):
    User.objects.all().delete()
    User.objects.create(username="Bob").save()
    User.objects.create(username="Leah").save()
    User.objects.create(username="Martin").save()

    users = User.objects.all()
    context = {"users": users}
    return render(request, 'pages/index.html', context)
