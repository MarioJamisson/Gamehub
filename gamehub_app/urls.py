from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar-jogos/', views.listar_jogos, name='listar_jogos'),
]
