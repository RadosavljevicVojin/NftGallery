


from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  # Uvozite pogled iz exhibitions app

urlpatterns = [
    path("login", accounts_views.login_page, name="login"),
    path("register", accounts_views.register_page, name="register")

]
