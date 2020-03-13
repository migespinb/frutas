"""frutas URL Configuration

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
from django.urls import path
from ventas import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.login),
    path('config/', views.config),
    path('logout/', views.logouts),
    path('', views.index),
    path('frutas/', views.frutas),
    path('ventas/', views.ventas),
    path('stocks/', views.stocks),
    path('createfruta/', views.createfruta),
    path('viewfruta/<int:id>', views.viewfruta),
    path('updatefruta/<int:id>', views.updatefruta),
    path('deletefruta/<int:id>', views.deletefruta),
    path('createventa/', views.createventa),
    path('viewventa/<int:id>', views.viewventa),
    path('updateventa/<int:id>', views.updateventa),
    path('deleteventa/<int:id>', views.deleteventa),
    path('createstock/', views.createstock),
    path('deletestock/<int:id>', views.deletestock),
    path('getprecio/', views.obtener_precio),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
