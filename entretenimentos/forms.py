from django import forms
from .models import Entretenimento

class EntretenimentoForm(forms.ModelForm):
    class Meta:
        model = Entretenimento
        fields = ['tipo', 'descricao']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }
