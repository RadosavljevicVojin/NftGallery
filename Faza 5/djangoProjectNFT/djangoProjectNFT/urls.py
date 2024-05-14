"""
URL configuration for djangoProjectNFT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from exhibitions import views as exhibitions_views  # Uvozite pogled iz exhibitions app
from accounts import views as accounts_views  # Uvozite pogled iz exhibitions app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', exhibitions_views.home_page, name='home'),
    path('accounts/', include('accounts.urls')),
    path('login', accounts_views.login_page, name='login1')
     # path('nft/', include('nft.urls')),
     # path('profiles/', include('profiles.urls')),
    # Dodajte ostale rute po potrebi
]
