from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact, Registration

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=["nom", "prénom", "email", "numéro_de_téléphone", "pays",]
        widget={
            'nom': TextInput(attrs={'class': 'form-control'}), 
            'prénom': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'numéro_de_téléphone': NumberInput(attrs={'class': 'form-control'})
        }