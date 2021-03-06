"""Technology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Users import views as Users_views
from posts import views as posts_views
from Profile import views as Profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', Profile_views.index, name='profile-home'),
    path('confirmation/', Profile_views.index, name='confirmation_page'),
    path('home/', Profile_views.home_index, name='home_index'),
    path('register/', Users_views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('posts/', posts_views.post_page, name='post_page'),
    
]
