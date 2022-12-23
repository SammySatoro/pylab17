from .models import Arena, Artist, Show, Ticket, Visitor
from django.forms import ModelForm, TextInput

class ArenaForm(ModelForm):
    form_name = 'arena'

    class Meta:
        model = Arena
        fields = ['Name', 'Location']
        widgets = {
            'ID': TextInput(attrs={
                'style': 'margin: 0 0 0 5% ',
                'class': 'form-control',
                'name': 'id',
                'placeholder': 'ID'}),
            'Name': TextInput(attrs={
                'style': 'margin: 0 0 0 5% ',
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Name'
            }),
            'Location': TextInput(attrs={
                'style': 'margin: 0 5% 0 5% ',
                'class': 'form-control',
                'name': 'location',
                'placeholder': 'Location'
            }),
        }