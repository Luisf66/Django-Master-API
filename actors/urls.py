from django.urls import path
from . import views

urlpatterns = [
     # url listar e cadastrar atores
    path('actors/', views.ActorListCreateView.as_view(), name='actor'),
    # url buscar, atualizar e deletar atores
    path('actors/<int:pk>', views.ActorRetrieveUpdateDestroyView.as_view(), name='acotr-detail-view'),
]