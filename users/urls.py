from django.urls import path, include
#from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'

urlpatterns = [
 #Include django default urls
   path('', include('django.contrib.auth.urls')),

 # Log out 
   path('logout_user/', views.logout_user, name='logout'),
   #path('users/logout/', LogoutView.as_view(), name='logout'),
    
 # Registration page.
    path('register/', views.register, name='register'),
]