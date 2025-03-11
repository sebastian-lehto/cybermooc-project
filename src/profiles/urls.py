from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>', views.profileView, name='profile'),    
    path('delete/<str:username>', views.deleteView, name='delete'),
    path("signup", SignUpView.as_view(), name="signup"),

]