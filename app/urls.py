from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('add-grade/', views.add_grade, name='add_grade'),
    path('', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'), 
]
