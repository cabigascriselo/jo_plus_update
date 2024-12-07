from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
 #Include django default urls
    path('', include('django.contrib.auth.urls')),

 # Log out 
    path('logout/', views.logout, name='logout'),
    
 # Registration page.
    path('register/', views.register, name='register'),
]