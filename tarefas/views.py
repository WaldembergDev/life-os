from django.shortcuts import redirect, render, get_object_or_404
from .forms import TarefaForm
from django.contrib import messages
from .models import Tarefa
from django.http import JsonResponse

# Create your views here.
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('criar_tarefa')
    else:
        form = TarefaForm()
    context = {
        'form': form
    }
    return render(request, 'tarefas/criar_tarefa.html', context=context)

def visualizar_tarefas(request):
    tarefas = Tarefa.objects.all()
    context = {
        'tarefas': tarefas,
        'form': TarefaForm()
    }
    return render(request, 'tarefas/visualizar_tarefas.html', context=context)

def excluir_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('visualizar_tarefas')

def api_consultar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    dados = {
        'tipo': tarefa.tipo,
        'criado_em': tarefa.criado_em,
        'nome': tarefa.nome,
        'prioridade':tarefa.prioridade,
        'status': tarefa.status,
        'prazo': tarefa.prazo,
        'com_lembrete': tarefa.com_lembrete
    }
    return JsonResponse(dados)

def editar_tarefa(request, id_tarefa):
    # 1. Recuperar a instância da Tarefa
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)

    if request.method == 'POST':
        # 2. POST: Passa request.POST E a instância da tarefa sendo editada
        form = TarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            form.save()
            messages.success(request, f'Tarefa "{tarefa.nome}" atualizada com sucesso!')
            
            return redirect('visualizar_tarefas') 
            
    else:
        form = TarefaForm(instance=tarefa) 

    context = {
        'form': form,
        'tarefa': tarefa
    }
    return render(request, 'tarefas/criar_tarefa.html', context)