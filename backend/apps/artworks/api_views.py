from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkListCreateAPI(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]


class ArtworkDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAuthenticated]