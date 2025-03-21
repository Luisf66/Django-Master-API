from movies.models import Movie
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieSerializer
# Create your views here.

class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer