"""ISTG_MADAY_OLIVO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from inicioApp import views

urlpatterns = [
    path('', views.inicioDef, name='iniciouRL'),
    path('musica', views.musicaDef, name='musicaUrl'),
    path('viajar', views.viajarDef, name='viajarUrl'),
    path('pensamiento', views.pensamientoDef, name='pensamientoUrl'),
    path('video', views.videoDef, name='videoUrl'),
    path('admin/', admin.site.urls),
]
