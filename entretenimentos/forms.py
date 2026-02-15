from django import forms
from .models import Entretenimento

class EntretenimentoCreateForm(forms.ModelForm):
    class Meta:
        model = Entretenimento
        fields = ['tipo', 'descricao']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'})
        }

class EntretenimentoUpdateForm(forms.ModelForm):
    class Meta:
        model = Entretenimento
        fields = '__all__'
        
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
