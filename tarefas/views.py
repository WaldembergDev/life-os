from django.shortcuts import redirect, render, get_object_or_404
from .forms import TarefaForm, SubtarefaForm, ComentarioForm
from django.contrib import messages
from .models import PrioridadeEnum, StatusEnum, Tarefa
from django.http import JsonResponse
from django.db.models import Case, When, IntegerField, Value
from .models import StatusEnum, Comentario
from .utils import obter_string_status_enum
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def tarefa_create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('tarefa_list')
    else:
        form = TarefaForm()
    context = {
        'form': form
    }
    return render(request, 'tarefas/tarefa_create.html', context=context)

@login_required
def tarefa_list(request):
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

    return render(request, 'tarefas/tarefas_list.html', context=context)

@login_required
def detalhe_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('detalhe_tarefa', id_tarefa)
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
    return redirect('tarefa_list')


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
def visualizar_tarefa(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        pass
    else:
        form = TarefaForm(instance=tarefa)
    context = {
        'form': form
    }
    return render(request, 'tarefas/visualizar_tarefa.html', context=context)


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


@login_required
def comentario_list(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    comentarios = Comentario.objects.filter(tarefa=tarefa)
    context = {
        'comentarios': comentarios,
        'tarefa': tarefa,
        'form': ComentarioForm()
    }
    return render(request, 'tarefas/comentario_list.html', context=context)

@login_required
def comentario_create(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, pk=id_tarefa)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            novo_comentario = form.save(commit=False)
            novo_comentario.tarefa = tarefa
            novo_comentario.save()
            messages.success(request, 'Comentário criado com sucesso!')
            return redirect('comentario_list', tarefa.id)
    else:
        form = ComentarioForm()
    context = {
        'form': form,
        'tarefa': tarefa
    }
    return render(request, 'tarefas/comentario_create.html', context=context)

@require_POST
@login_required
def comentario_delete(request, id_comentario):
    comentario = get_object_or_404(Comentario, id=id_comentario)
    comentario.delete()
    messages.success(request, 'Comentário excluído com sucesso!')
    # return redirect('comentario_list', comentario.tarefa.id )
    return JsonResponse({'mensagem': 'Comentário Excluído!'})
