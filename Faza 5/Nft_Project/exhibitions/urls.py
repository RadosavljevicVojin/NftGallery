from django.urls import path
from exhibitions import views as exhibitions_views

urlpatterns = [
    path('', exhibitions_views.index, name="index"),
    path('exhibitions/create_exhibition', exhibitions_views.create_exhibition, name="create_exhibition"),
    path('exhibitions/change_exhibition/<int:exhibition_id>', exhibitions_views.change_exhibition, name="change_exhibition"),
    path('exhibitions/sort_index', exhibitions_views.sort_index, name="sort_index")
]