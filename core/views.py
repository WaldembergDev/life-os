from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as as_login, logout as as_logout, authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('pagina_inicial')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('senha')
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 as_login(request, user)
#                 return redirect('pagina_inicial')
#             else:
#                 messages.error(request, 'Login ou senha inválidos!')
#     else:
#         form = LoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'core/login.html', context)


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
