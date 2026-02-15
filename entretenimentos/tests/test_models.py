from django.test import TestCase
from ..models import Entretenimento, CustomUser

# Create your tests here.
class EntretenimentoTestCase(TestCase):
    def setUp(self):
        usuario = CustomUser.objects.create_user(
            email='waldemberg@gmail.com',
            password='123456'
        )
        self.entretenimento = Entretenimento.objects.create(
            tipo=Entretenimento.Tipo.FILME,
            descricao='Vingadores',
            criado_por=usuario
        )
    
    def test_entretenimento_atualizar_automaticamente_concluido_em(self):
        # entretenimento = Entretenimento.objects.get(id=1)
        self.entretenimento.status = Entretenimento.Status.CONCLUIDO
        self.entretenimento.save()
        # verificando se o campo finalizado_em é preenchido automaticamente
        self.assertIsNotNone(self.entretenimento.finalizado_em, msg='Finalizado em está vazio!')

        # verificando se o campo finalizado_em é alterado automaticamente para None
        self.entretenimento.status = Entretenimento.Status.PENDENTE
        self.entretenimento.save()
        self.assertIsNone(self.entretenimento.finalizado_em, msg="Finalizado em está preenchido!")