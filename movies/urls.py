from django.urls import path
from . import views

urlpatterns = [
    # url listar e cadastrar filmes
    path('movies/', views.MovieListCreateView.as_view(), name='movie'),
    # url buscar, atualizar e deletar filmes
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail.view'),
]