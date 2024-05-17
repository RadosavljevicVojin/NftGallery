from django.urls import path, include
from nft import views as nft_views

urlpatterns = [
    path("create_nft", nft_views.create_nft, name="create_nft"),

]
