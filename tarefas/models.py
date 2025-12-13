from django.db import models
from django.utils import timezone
from core.models import CustomUser

class TipoEnum(models.TextChoices):
    PESSOAL = 'PESSOAL', 'Pessoal'
    PROFISSIONAL = 'PROFISSIONAL', 'Profissional'

class PrioridadeEnum(models.TextChoices):
    URGENTE = 'URGENTE', 'Urgente'
    NORMAL = 'NORMAL', 'Normal'
    BAIXO = 'BAIXO', 'Baixo'

class StatusEnum(models.TextChoices):
    PENDENTE = 'PENDENTE', 'Pendente'
    ANDAMENTO = 'ANDAMENTO', 'Andamento'
    CONCLUIDO = 'CONCLUIDO', 'Concluído'

# Create your models here.
class Tarefa(models.Model):
    tipo = models.CharField(max_length=12, choices=TipoEnum.choices, default=TipoEnum.PESSOAL)
    criado_em = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=120)
    prioridade =models.CharField(max_length=9, choices=PrioridadeEnum.choices, default=PrioridadeEnum.NORMAL)
    status = models.CharField(max_length=9, choices=StatusEnum.choices, default=StatusEnum.PENDENTE)
    concluido_em = models.DateTimeField(null=True, blank=True)
    prazo = models.DateField(null=True, blank=True)
    com_lembrete = models.BooleanField(default=True)
    criador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.status == StatusEnum.CONCLUIDO:
            if not self.concluido_em:
                self.concluido_em = timezone.now()
        else:
            self.concluido_em = None
        super(Tarefa, self).save(*args, *kwargs)

class Comentario(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=255)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario