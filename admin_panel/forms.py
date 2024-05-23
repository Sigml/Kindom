from django import forms
from game.models import (Age, Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)


class AgeCreateForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = ('name', 'start_of_era', 'end_of_era',)
        labels = {
            'name': 'Nazwa epoki',
            'start_of_era': 'Data początku epoki',
            'end_of_era': 'Data końca epoki',
        }
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
        labels = {
            'name': 'Nazwa kraju',
            'capital': 'Kapitał',
            'population': 'Ilość mieskanców',
            'income': 'Dochód',
        }
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
        labels = {
            'country': 'Nazwa państwa',
            'name': 'Nazwa zasobu',
            'quantity': 'Ilość',
            'price': 'Cena',
        }
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
        

class FactoryCreateForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ('name', 'image', )
        labels = {
            'name':'Nazwa fabryki',
            'image':'Obrazek fabryki',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa fabryki'
            })
        }
        
        
class RequiredResourcesCreateForm(forms.ModelForm):
    class Meta:
        model = RequiredResources
        fields = ('resource', 'required_resource', 'quantity',)
        labels = {
            'resource':'Zasób',
            'required_resource':'Wymagany zasób',
            'quantity':'ILość',
        }
        widgets = {
            'required_resource':forms.Select(attrs={
                'class':'form-control'
            }),
            'resource':forms.Select(attrs={
                'class':'form-control'
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control'
            })
        }
        
        
class BuildFactoryCreateForm(forms.ModelForm):
    class Meta:
        model = BuildFactory
        fields = ('factory', 'age', 'resources_production', 'required_resource_1', 'quantity_required_resource_1',
                  'required_resource_2', 'quantity_required_resource_2', 'required_resource_3', 'quantity_required_resource_3',)
        labels = {
            'factory':'Fabryka', 
            'age':'Epoka',
            'resources_production':'Produkujący się zasob', 
            'required_resource_1':'Zasob dla budowy nr 1',
            'quantity_required_resource_1':'Ilość',
            'required_resource_2':'Zasob dla budowy nr 2', 
            'quantity_required_resource_2':'Ilość', 
            'required_resource_3':'Zasob dla budowy nr 3', 
            'quantity_required_resource_3':'Ilość',
        }
        widgets = {
            'factory':forms.Select(attrs={
                'class':'form-control'
            }),
            'age':forms.Select(attrs={
                'class':'form-control'
            }),
            'resources_production':forms.Select(attrs={
                'class':'form-control'
            }),
            'required_resource_1':forms.Select(attrs={
                'class':'form-control'
            }), 
            'quantity_required_resource_1':forms.NumberInput(attrs={
                'class':'form-control'
            }),
             'required_resource_2':forms.Select(attrs={
                'class':'form-control'
            }),
             'quantity_required_resource_2':forms.NumberInput(attrs={
                'class':'form-control'
            }),
             'required_resource_3':forms.Select(attrs={
                'class':'form-control'
            }),
             'quantity_required_resource_3':forms.NumberInput(attrs={
                'class':'form-control'
            })
        }