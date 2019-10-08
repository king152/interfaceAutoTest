from django.urls import path
from userinfo import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('check/', views.check, name='check'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_operate/', views.user_operate, name='user_operate'),
    path('logout/', views.logout, name='logout'),
]
