from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout_view/', views.logout_view, name='logout_view'),
]