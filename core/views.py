from django.shortcuts import render, redirect
from django.contrib.auth import logout as as_logout
from django.contrib.auth.decorators import login_required


@login_required
def pagina_inicial(request):
    return render(request, 'core/pagina_inicial.html')

def logout(request):
    as_logout(request)
    return redirect('two_factor:login')

@login_required
def visualizar_perfil(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'core/perfil.html', context)