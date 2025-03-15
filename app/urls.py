"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# view dos filmes
from movies.views import MovieListCreateView, MovieRetrieveUpdateDestroyView
# view das reviews
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    # url admin
    path('admin/', admin.site.urls),
    # url dos generos
    path('api/v1/', include('genres.urls')),
    # url dos atores
    path('api/v1/', include('actors.urls')),
    # url listar e cadastrar filmes
    path('movies/', MovieListCreateView.as_view(), name='movie'),
    # url buscar, atualizar e deletar filmes
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail.view'),
    # url listar e cadastrar reviews
    path('reviews/', ReviewListCreateView.as_view(), name='review'),
    # url buscar, atualizar e deletar reviews
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]