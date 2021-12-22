"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('mujer-remeras/', views.Mremeras, name="mujer-remeras"),
    path('mujer-jeans/', views.Mjeans, name="mujer-jeans"),
    path('mujer-camisetas/', views.Mcamisetas, name="mujer-camisetas"),
    path('mujer-calzas', views.Mcalzas, name="mujer-calzas"),
    path('mujer-joggins/', views.Mjoggins, name="mujer-joggins"),
    path('mujer-pijamas/', views.Mpijamas, name="mujer-pijamas"),
    path('hombre-remeras/', views.Hremeras, name="hombre-remeras"),
    path('hombre-jeans/', views.Hjeans, name="hombre-jeans"),
    path('hombre-joggins/', views.Hjoggins, name="hombre-joggins"),
    path('hombre-camisetas/', views.Hcamisetas, name="hombre-camisetas"),
    path('accesorios-mochilas/', views.Amochilas, name="accesorios-mochilas"),
    path('accesorios-bolsos/', views.Abolsos, name="accesorios-bolsos"),
    path('accesorios-riñoneras/', views.Ariñoneras, name="accesorios-riñoneras"),
    path('accesorios-bandoleras/', views.Abandoleras, name="accesorios-bandoleras"),
    path('ofertas/', views.Ofertas, name="ofertas"),
    path('registro/', views.Registro_usuarios, name="registro"),
    path('login/', views.Login_Page, name="login"),
    path('logout/', views.Logout_user, name="logout")  
]
