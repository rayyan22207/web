from django.urls import path
from  . import views

from django.urls import reverse



urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

 
    path('', views.home, name="home"),
    path('the_makking_of_a_room/', views.createRoom, name="creat_room"),

    
    path('profile/<str:pk>/', views.userProfile, name="user-profile",),
    

]
