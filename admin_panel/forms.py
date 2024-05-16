from django import forms
from game.models import (Age, Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)


class AgeCreateForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = ('name', 'start_of_era', 'end_of_era',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa epoki'
            }),
            'start_of_era': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Data początku epoki'
            }),
            'end_of_era': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Data konca epoki'
            }),
        }
        

class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'capital', 'population', 'income',)
        Widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa kraju'
            }),
            'capital': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Kapitał'
            }),
            'population': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ilość mieskanców'
            }),
            'income': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Dochód'
            }),
        }
        

class ResourcesCreateForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ('country', 'name', 'quantity', 'price',)
        widgets = {
            'country': forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Nazwa państwa'
                }),
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa zasobu'
                }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Ilość'
                }),
            'price':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Cena'
                }),
        }