from django.shortcuts import redirect, render, get_object_or_404
from .forms import TarefaForm
from django.contrib import messages
from .models import PrioridadeEnum, StatusEnum, Tarefa
from django.http import JsonResponse
from django.db.models import Case, When, IntegerField, Value
from .models import StatusEnum
from .utils import obter_string_status_enum
from django.urls import reverse

# Create your views here.
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('criar_tarefa')
    else:
        form = TarefaForm()
    context = {
        'form': form
    }
    return render(request, 'tarefas/criar_tarefa.html', context=context)

def visualizar_tarefas(request):
    status = request.GET.get('status')
    # ordenando do vencimento mais próximo para o mais antigo e urgência

    tarefas = Tarefa.objects.annotate(
        tarefa_classificada = Case(
            When(prioridade=PrioridadeEnum.URGENTE, then=1),
            When(prioridade=PrioridadeEnum.NORMAL, then=2),
            When(prioridade=PrioridadeEnum.BAIXO, then=3),
            When(prazo__isnull=False, then=4),
            default=5,
            output_field=IntegerField()
        )
    ).order_by('tarefa_classificada', 'prazo')

    # verificando se existe um status válido selecionado
    if status and (obter_string_status_enum(status) is not None):
        tarefas = tarefas.filter(status=obter_string_status_enum(status))

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
        'com_lembrete': tarefa.com_lembrete,
        'concluido_em': tarefa.concluido_em
    }
    return JsonResponse(dados)

def editar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)

    if request.method == 'POST':
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

def concluir_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.status = StatusEnum.CONCLUIDO
    tarefa.save()
    messages.success(request, 'Tarefa marcada com status concluída')
    return redirect(reverse('visualizar_tarefas'))
