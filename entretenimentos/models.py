from django.db import models
from core.models import CustomUser
from django.utils import timezone

# Create your models here.
class Entretenimento(models.Model):
    class Tipo(models.TextChoices):
        FILME = 'FILME', 'Filme'
        SERIE = 'SERIE', 'Série'
        LIVRO = 'LIVRO', 'Livro'
        JOGO = 'JOGO', 'Jogo'
        CULTURA = 'CULTURA', 'Cultura'
    
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        ANDAMENTO = 'ANDAMENTO', 'Andamento'
        CONCLUIDO = 'CONCLUIDO', 'Concluído'
    
    criado_em = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=Tipo.choices, verbose_name='Tipo')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)
    iniciado_em = models.DateTimeField(null=True, blank=True)
    finalizado_em = models.DateTimeField(null=True, blank=True)
    criado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
    
    def save(self, *args, **kwargs):
        if self.status == Entretenimento.Status.CONCLUIDO:
            self.finalizado_em = timezone.now()
        if self.status != Entretenimento.Status.CONCLUIDO:
            self.finalizado_em = None
        super(Entretenimento, self).save(*args, **kwargs)