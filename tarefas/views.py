from django.shortcuts import redirect, render, get_object_or_404
from .forms import TarefaForm, SubtarefaForm
from django.contrib import messages
from .models import PrioridadeEnum, StatusEnum, Tarefa
from django.http import JsonResponse
from django.db.models import Case, When, IntegerField, Value
from .models import StatusEnum
from .utils import obter_string_status_enum
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('visualizar_tarefas')
    else:
        form = TarefaForm()
    context = {
        'form': form
    }
    return render(request, 'tarefas/criar_tarefa.html', context=context)

@login_required
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
    if not status:
        status = 'pendente'
        tarefas = tarefas.filter(status=StatusEnum.PENDENTE.value)

    context = {
        'tarefas': tarefas,
        'form': TarefaForm(),
        'status': status,
    }

    return render(request, 'tarefas/visualizar_tarefas.html', context=context)

@login_required
def detalhe_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        pass
    else:
        form = TarefaForm(instance=tarefa)
    context = {
        'form': form
    }
    return render(request, 'tarefas/tarefa_detail.html', context)


@login_required
def excluir_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('visualizar_tarefas')


@login_required
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

@login_required
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


@login_required
def criar_subtarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = SubtarefaForm(request.POST)
        if form.is_valid():
            subtarefa = form.save(commit=False)
            subtarefa.tarefa = tarefa
            subtarefa.save()
            return redirect('visualizar_tarefas')
    else:
        subtarefa = SubtarefaForm()
    
    context = {
        'form': subtarefa
    }
    return render(request, 'tarefas/criar_subtarefa.html', context)
