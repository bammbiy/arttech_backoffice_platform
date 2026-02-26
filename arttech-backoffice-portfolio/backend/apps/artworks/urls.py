from django.urls import path
from . import views

urlpatterns = [
    path("", views.artwork_list, name="artwork_list"),
    path("create/", views.artwork_create, name="artwork_create"),
    path("delete/<int:pk>/", views.artwork_delete, name="artwork_delete"),
]