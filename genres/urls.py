from django.urls import path
from . import views

urlpatterns = [
    # url listar e cadastrar generos 
    path('genres/', views.GenreCreateListView.as_view(), name='genre'),
    # url buscar, atualizar e deletar generos
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]