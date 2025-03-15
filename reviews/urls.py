from django.urls import path
from . import views

urlpatterns = [
    # url listar e cadastrar reviews
    path('reviews/', views.ReviewListCreateView.as_view(), name='review'),
    # url buscar, atualizar e deletar reviews
    path('reviews/<int:pk>', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]
