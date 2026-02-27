from django.urls import path
from .api_views import ArtworkListCreateAPI, ArtworkDetailAPI

urlpatterns = [
    path("", ArtworkListCreateAPI.as_view(), name="api_artwork_list"),
    path("<int:pk>/", ArtworkDetailAPI.as_view(), name="api_artwork_detail"),
]