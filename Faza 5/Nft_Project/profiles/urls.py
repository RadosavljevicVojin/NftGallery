from django.urls import path, include
from profiles import views as profiles_view

urlpatterns = [
    path("profile_info", profiles_view.view_profile_info, name="profile_info"),
    path("profile_collection", profiles_view.view_profile_collection, name="profile_collection"),
    path("profile_portfolio", profiles_view.view_profile_portfolio, name="profile_portfolio"),
    path("profile_exhibitions", profiles_view.view_profile_exhibitions, name="profile_exhibitions"),

]
