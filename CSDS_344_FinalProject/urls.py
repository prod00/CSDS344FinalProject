"""CSDS_344_FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from main_site.views import home, teacher_login, login_redirect, teacher_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('teacher_login/', teacher_login, name="teacher_login"),
    path('teacher_login/redirect', login_redirect, name="tl_redirect"),
    path('teacher_home', teacher_home, name="teacher_home"),
]
