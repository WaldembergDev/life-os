from django.urls import path
from . import views

urlpatterns = [
    path('criar-tarefa/', views.tarefa_create, name='tarefa_create'),
    path('visualizar-tarefas/', views.tarefa_list, name='tarefa_list'),
    path('excluir-tarefa/<int:id_tarefa>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('api-consultar-tarefa/<int:id_tarefa>/', views.api_consultar_tarefa, name='api_consultar_tarefa'),
    path('editar-tarefa/<int:id_tarefa>/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:id_tarefa>/', views.detalhe_tarefa, name="detalhe_tarefa"),
    path('<int:id_tarefa>/comentarios/', views.comentario_list, name='comentario_list'),
    path('<int:id_tarefa>/criar-comentario/', views.comentario_create, name='comentario_create')
]