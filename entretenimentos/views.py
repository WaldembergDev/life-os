from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Entretenimento
from .forms import EntretenimentoUpdateForm, EntretenimentoCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def entretenimento_create(request):
    """ view que cria um entretenimento """
    if request.method == 'POST':
        form = EntretenimentoCreateForm(request.POST)
        if form.is_valid():
            entretenimento = form.save(commit=False)
            entretenimento.criado_por = request.user
            entretenimento.save()
            messages.success(request, 'Entretenimento criado com sucesso!')
            return redirect('entretenimento_create')
    else:
        form = EntretenimentoCreateForm()
    context = {
        'form': form
    }
    return render(request, 'entretenimentos/entretenimento_create.html', context)

@login_required
def entretenimento_list(request):
    """ view que exibe os entrenimentos do sistema """
    entretenimentos = Entretenimento.objects.all()
    context = {
        'entretenimentos': entretenimentos
    }
    return render(request, 'entretenimentos/entretenimento_list.html', context)

@login_required
def entretenimento_detail(request, id_entretenimento) -> HttpResponse:
    """
    Detalha o entretenimento selecionado e permite sua atualização 

    Args:
        request: O objeto HttpRequest do Django
        id_entretenimento: O id do entretenimento selecionado
    
    
    Returns:
        HttpResponse: Renderiza o template de detalhe do entretenimento
    """
    entretenimento = get_object_or_404(Entretenimento, id=id_entretenimento)
    if request.method == 'POST':
        form = EntretenimentoUpdateForm(request.POST, instance=entretenimento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entretenimento atualizado com sucesso!')
            return redirect('entretenimento_list')
    else:
        form = EntretenimentoUpdateForm(instance=entretenimento)
    context = {
        'form': form
    }
    return render(request, 'entretenimentos/entretenimento_detail.html', context)    