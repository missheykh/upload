from django.contrib import admin
from django.urls import path,include
from .views import login,show_files,logout,register

app_name="file"

urlpatterns = [
    
    path("login/",login,name="login"),
    path("logout/",logout,name="logout"),
    path("register/",register,name="register"),
    path("show_files/",show_files,name="show_files"),
]
