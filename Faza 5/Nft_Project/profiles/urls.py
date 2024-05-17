from django.urls import path, include
from profiles import views as profiles_view

urlpatterns = [
    path("profile", profiles_view.view_profile, name="profile"),

]
