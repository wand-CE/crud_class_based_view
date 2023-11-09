from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('cadastroproduto/', views.ProdutoCreateView.as_view(), name='cadproduto'),
    path('meusprodutos/', views.ProdutoListView.as_view(), name='listarprodutos'),
    path('atualizarproduto/<int:pk>/', views.ProdutoUpdateView.as_view(), name='atualizarproduto'),
    path('excluirproduto/<int:pk>/', views.ProdutoDeleteView.as_view(), name='excluirproduto'),
]