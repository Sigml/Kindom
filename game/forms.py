from django import forms
from .models import NewWorld

class NewWorldForm(forms.ModelForm):
    class Meta:
        model = NewWorld
        fields = ['country', 'age']