from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponse

@login_required(login_url='profiles/login')
def index(request):
    User = get_user_model()
    users = User.objects.exclude(username="admin")
    context = {"users": users}
    
    return render(request, 'index.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required(login_url='profiles/login')
def profileView(request, username):
    User = get_user_model()
    profile = User.objects.get(username=username)
    context = {"profile": profile}
    return render(request, 'profile.html', context)

def deleteView(request, username):
    if not request.user.is_superuser:
        return redirect("/")

        #!!!!!!!!!!!!
    User = get_user_model()
    User.objects.get(username=username).delete()

    users = User.objects.exclude(username="admin")
    context = {"users": users}
    return render(request, 'index.html', context)

