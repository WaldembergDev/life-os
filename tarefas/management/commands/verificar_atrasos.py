from django.core.management.base import BaseCommand
from django.utils import timezone
from tarefas.models import Tarefa, StatusEnum
from notificacoes.services import Whapi

class Command(BaseCommand):
    help = 'Verifica tarefas atrasadas e envia notificação via WhatsApp'

    def handle(self, *args, **kwargs):
        # verificando as tarefas atrasadas
        self.stdout.write("Iniciando verificação de atrasos...")
        tarefas_atrasadas = Tarefa.objects.filter(prazo__lt=timezone.now().date()).exclude(status=StatusEnum.CONCLUIDO.value).exclude(com_lembrete=False)
        self.stdout.write("Verificação concluída.")

        # personalizando a mensagem a ser enviada
        self.stdout.write("Personalizando a mensagem...")
        mensagem = "*Notificação de tarefas atrasadas*\n"
        
        if tarefas_atrasadas:
            for tarefa in tarefas_atrasadas:
                texto = f'Tarefa: {tarefa.nome} - prazo: {tarefa.prazo.strftime("%d/%m/%Y")}\n'
                mensagem += texto
        else:
            mensagem += 'Não há tarefas atrasadas'
        self.stdout.write("Mensagem personalizada concluída...")
        
        # enviando a mensagem pelo whatsapp
        self.stdout.write('Enviando a mensagem pelo Whatsapp')
        notificacao_whatsapp = Whapi()
        notificacao_whatsapp.enviar_mensagem_texto(mensagem)
        self.stdout.write('Mensagen enviada')