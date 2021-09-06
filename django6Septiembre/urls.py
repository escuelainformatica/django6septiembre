"""django6Septiembre URL Configuration

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

import st_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/',st_app.views.Listado.as_view()),
    path('auto/insertar',st_app.views.Insertar.as_view()),
    path('auto/modificar/<int:id>',st_app.views.Modificar.as_view()),
    path('auto/eliminar/<int:id>',st_app.views.Eliminar.as_view()),
]
