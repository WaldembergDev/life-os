from django.shortcuts import redirect, render
from .forms import TarefaForm
from django.contrib import messages
from .models import Tarefa

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
        'tarefas': tarefas
    }
    return render(request, 'tarefas/visualizar_tarefas.html', context=context)