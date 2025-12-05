from django.db import models

class TipoEnum(models.TextChoices):
    PESSOAL = 'PESSOAL', 'Pessoal'
    PROFISSIONAL = 'PROFISSIONAL', 'Profissional'

class PrioridadeEnum(models.TextChoices):
    URGENTE = 'URGENTE', 'Urgente'
    ALTO = 'ALTO', 'Alto'
    NORMAL = 'NORMAL', 'Normal'
    BAIXO = 'BAIXO', 'Baixo'
    PLANEJADO = 'PLANEJADO', 'Planejado'

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
    prazo = models.DateField(null=True, blank=True)
    com_lembrete = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    comentario = models.CharField(max_length=255)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario