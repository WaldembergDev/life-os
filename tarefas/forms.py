from django import forms
from .models import Tarefa, Comentario

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['tipo', 'nome', 'prioridade', 'status', 'prazo', 'com_lembrete']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'com_lembrete': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
