from django.urls import path
from . import views

urlpatterns = [
    path('criar-tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('visualizar-tarefas/', views.visualizar_tarefas, name='visualizar_tarefas')
]