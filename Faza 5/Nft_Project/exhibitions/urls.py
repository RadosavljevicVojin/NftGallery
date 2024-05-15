from django.urls import path

from exhibitions import views

urlpatterns = [
    path('', views.index, name="index")
]