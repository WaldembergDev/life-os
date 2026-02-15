from django.shortcuts import render, redirect
from .models import Entretenimento
from .forms import EntretenimentoForm
from django.contrib import messages

# Create your views here.
def entretenimento_create(request):
    """ view que cria um entretenimento """
    if request.method == 'POST':
        form = EntretenimentoForm(request.POST)
        if form.is_valid():
            entretenimento = form.save(commit=False)
            entretenimento.criado_por = request.user
            entretenimento.save()
            messages.success(request, 'Entretenimento criado com sucesso!')
            return redirect('entretenimento_create')
    else:
        form = EntretenimentoForm()
    context = {
        'form': form
    }
    return render(request, 'entretenimentos/entretenimento_create.html', context)

def entretenimento_list(request):
    """ view que exibe os entrenimentos do sistema """
    entretenimentos = Entretenimento.objects.all()
    context = {
        'entretenimentos': entretenimentos
    }
    return render(request, 'entretenimentos/entretenimento_list.html', context)
