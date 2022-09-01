from logging import PlaceHolder
from django import forms
from .models import Ecosystem

class EcosystemForm(forms.ModelForm):
    #widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    class Meta:
        model = Ecosystem
        fields = ('ecosystem_name', 'location', 'template_name',)

        widgets = {
            'ecosystem_name': forms.TextInput(attrs={'placeholder': 'school name'}),
            'location': forms.TextInput(
                attrs={'placeholder': 'city, state'}),
        }