"""
URL configuration for funeducare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from aboutus import views
from contactus import views
from home import views
from payments import views
from pendaftaran import views
from profil import views
from programs import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('contactus/', include('contactus.urls')),
    path('', include('home.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('programs/', include('programs.urls')),
]
