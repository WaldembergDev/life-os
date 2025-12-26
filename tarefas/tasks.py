from .models import Tarefa, StatusEnum
from django.utils import timezone
from datetime import date
from notificacoes.services import Whapi

def obter_tarefas_atrasadas():
    tarefas_atrasadas = Tarefa.objects.filter(prazo__lt=timezone.now().date()).exclude(status=StatusEnum.CONCLUIDO.value)
    mensagem = "*Notificação de tarefas atrasadas*\n"
    if tarefas_atrasadas:
        for tarefa in tarefas_atrasadas:
            texto = f'Tarefa: {tarefa.nome} - prazo: {tarefa.prazo.strftime('%d/%m/%Y')}\n'
            mensagem += texto
    else:
        mensagem += 'Não há tarefas atrasadas'    
    notificacao_whatsapp = Whapi()
    notificacao_whatsapp.enviar_mensagem_texto(mensagem)