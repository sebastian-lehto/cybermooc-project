from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:uid>', views.profileView, name='profile'),    
    path('delete/<int:uid>', views.deleteView, name='delete'),
    #path('login', views.login, name='login'),
    #path('loginView', views.loginView, name='loginView'),
    #path('logout', views.logout, name='logout')

]