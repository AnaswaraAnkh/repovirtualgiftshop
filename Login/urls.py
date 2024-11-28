

from django.urls import path

from Login.views import Login_view,Sendotp

urlpatterns = [
    
    path('',Login_view.as_view(),name='Login_view'),
    path('Sendotp',Sendotp.as_view(),name='Sendotp'),
   
   
   
   ]
