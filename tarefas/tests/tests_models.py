from django.test import TestCase
from ..models import Tarefa, StatusEnum
from core.models import CustomUser
from datetime import date, timedelta

class TarefaTestCase(TestCase):
    def setUp(self):
        self.usuario = CustomUser.objects.create_user(email='waldemberg@gmail.com', password='123456')
        self.tarefa = Tarefa.objects.create(nome="Tarefa teste", criador=self.usuario)
    
    def test_atualizar_automaticame_data_concluido_em(self):
        # preparando
        self.tarefa.status = StatusEnum.CONCLUIDO
        # age
        self.tarefa.save()
        # verifica
        self.assertIsNotNone(self.tarefa.concluido_em)
    
    def test_remover_data_concluido_em(self):
        # preparando
        self.tarefa.status = StatusEnum.CONCLUIDO
        # age
        self.tarefa.save()
        self.tarefa.status = StatusEnum.PENDENTE
        self.tarefa.save()
        # verifica
        self.assertIsNone(self.tarefa.concluido_em, 'Passou no teste')

    def test_metodo_esta_vencido_prazo_passado_retorna_correto(self):
        self.tarefa.prazo = date.today() - timedelta(days=1)
        self.assertTrue(self.tarefa.esta_vencida)
    
    def test_metodo_esta_vencido_status_concluido_retorna_falso(self):
        self.tarefa.status = StatusEnum.CONCLUIDO
        self.tarefa.save()
        self.assertFalse(self.tarefa.esta_vencida)
        

        


