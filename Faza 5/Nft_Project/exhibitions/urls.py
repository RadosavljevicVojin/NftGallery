from django.urls import path
from exhibitions import views as exhibitions_views

urlpatterns = [
    path('', exhibitions_views.index, name="index"),
    path('exhibitions/create_exhibition', exhibitions_views.create_exhibition, name="create_exhibition")

]