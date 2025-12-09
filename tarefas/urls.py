from django.urls import path
from . import views

urlpatterns = [
    path('criar-tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('visualizar-tarefas/', views.visualizar_tarefas, name='visualizar_tarefas'),
    path('excluir-tarefa/<int:id_tarefa>', views.excluir_tarefa, name='excluir_tarefa'),
    path('api-consultar-tarefa/<int:id_tarefa>', views.api_consultar_tarefa, name='api_consultar_tarefa')
]