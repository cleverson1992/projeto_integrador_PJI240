from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="homepage"),
    path('cadastro_estoque/', views.cadastro_estoque, name="cadastro_estoque"),
    path('gerenciar_estoque/', views.gerenciar_estoque, name="gerenciar_estoque"),
    path('deletar/<int:id>', views.deletar)
]