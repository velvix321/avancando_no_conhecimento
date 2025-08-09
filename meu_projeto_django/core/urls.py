"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#1
from django.contrib import admin
from django.urls import path, include

#2
from rest_framework import routers
from tarefas.views import tarefaviewset

#2
router = routers.DefaultRouter()
router.register(r'tarefas', tarefaviewset)

#1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),
    path('api/', include(router.urls)),
    
    ]