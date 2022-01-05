from django.urls import  path
from .views import  registerView,profileView,UpdateProfileView,UpdateAccountView





urlpatterns = [
    path ('register/',registerView ,name='register'),
    path('profile', profileView, name='profile'),
    path('update_profile', UpdateProfileView.as_view(), name='update_profile'),
    path('update_account', UpdateAccountView.as_view(), name='update_account'),
    
    ]
