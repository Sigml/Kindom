from django import forms
from .models import NewWorld, Age

class NewWorldForm(forms.ModelForm):
    age = forms.ModelChoiceField(queryset=Age.objects.all(), label="Wiek", empty_label="Wybierz wiek")

    class Meta:
        model = NewWorld
        fields = ['country', 'age']
