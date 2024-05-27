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
        
        
class EcologyCreateForm(forms.ModelForm):
    class Meta:
        model = Ecology
        fields = ('country', 'air_quality', 'water_pollution', 'forest_coverage', 'wildlife_population')
        labels = {
            'country':'Państwo',
            'air_quality':'Stan powietrza',
            'water_pollution':'Stan wody',
            'forest_coverage':'Stan lasu',
            'wildlife_population':'Żywność',
        }
        widgets = {
            'country':forms.Select(attrs={
                'class':'form-control'
            }),
            'air_quality':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'water_pollution':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'forest_coverage':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'wildlife_population':forms.NumberInput(attrs={
                'class':'form-control'
            }),
        }
        
########
class TradeCreateForm(forms.ModelForm):
    class Meta:
        models = Trade
        fields = ('exporter', 'imports', 'resource',)
        labels = {
            'exporter':'eksporter',
            'imports':'import',
            'resource':'zasób',
        }
        widgets = {
            'exporter':forms.Select(attrs={
                'class':'form-control'
            }),
            'imports':forms.Select(attrs={
                'class':'form-control'
            }),
            'resource':forms.Select(attrs={
                'class':'form-control'
            }),
        }
        
        
class AllianceCreateForm (forms.ModelForm):
    class Meta:
        model = Alliance
        fields = ('name', 'members')
        labels = {
                'name':'Nazwa',
                'members':'Członkowie'
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'members':forms.SelectMultiple(attrs={
                'class':'form-control'
                }),
        }
        

class TradeAgreementCreateForm(forms.ModelForm):
    class Meta:
        model = TradeAgreement
        fields = ('alliance', 'participants', 'start_date', 'end_date',)
        labels = {
            'alliance':'Sojusz', 
            'participants':'Uczestnicy', 
            'start_date':'Data rozpoczęcia', 
            'end_date':'Data końcowa',
        }
widgets = {
            'alliance': forms.Select(attrs={
                'class': 'form-control'
            }),
            'participants': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
        }
        
        
class PeaceTreatyCreateForm (forms.ModelForm):
    class Meta:
        model = PeaceTreaty
        fields = ('country1', 'country2', 'start_date', 'end_date',)
        labels = {
            'country1':'Państwo',
            'country2':'Państwo',
            'start_date':'Data rozpoczęcia', 
            'end_date':'Data końcowa',
        }
        widgets = {
            'country1': forms.Select(attrs={
                'class': 'form-control'
            }),
            'country1':forms.Select(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
        }
        
        
class ArmyCreateForm (forms.ModelForm):
    class Meta:
        model = Army
        fields = ('country', 'name', 'quantity', 'power',)
        labels = {
            'country':'Państwo',
            'name': 'Nazwa wojska',
            'quantity':'Ilość', 
            'power':'Moc',
        }
        widgets = {
            'country':forms.Select(attrs={
                'class': 'form-control'
            }), 
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'power':forms.NumberInput(attrs={
                'class':'form-control'}),
        }
        
        
class WarCreateForm(forms.ModelForm):
    class Meta: 
        model = War
        fields = ('attacker', 'defender', 'start_date', 'end_date', 'status',)
        labels = {
            'attacker':'Atakujący',
            'defender':'Obrońca', 
            'start_date':'Data rozpoczęcia', 
            'end_date':'Data końcowa',
            'status':'stan',
        }
        widgets = {
            'attacker':forms.Select(attrs={
                'class': 'form-control'
            }),
            'defender':forms.Select(attrs={
                'class': 'form-control'
            }), 
            'start_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'status':forms.BooleanField(attrs={
                'class': 'form-control'
            }),
        }
        
        
class TechnologyCreateForm (forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('age', 'name', 'efficiency_production', 'efficiency_trade', 'efficiency_military',)
        labels = {
            'age':'Epoka',
            'name':'Nazma', 
            'efficiency_production':'Efektywność produkcji',
            'efficiency_trade':'Efektywność handlu',
            'efficiency_military':'Efektywność wojskowa',
        }
        widgets = {
            'age':forms.Select(attrs={
                'class': 'form-control'
            }),
            'name':forms.Select(attrs={
                'class':'form-control'
                }), 
            'efficiency_production':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'efficiency_trade':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'efficiency_military':forms.NumberInput(attrs={
                'class':'form-control'
                }),
        }
        
        
class EventCreateForm (forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'impact_economy', 'impact_society', 'impact_military',)
        labels = {
            'name':'Nazwa',
            'description':'Opis',
            'impact_economy':'Wpływ gospodarczy', 
            'impact_society':'Wpływ społeczeństwa',
            'impact_military':'Wpływ wojskowy',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'description':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'impact_economy':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'impact_society':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'impact_military':forms.NumberInput(attrs={
                'class':'form-control'
                }),
        }
        
    
class SocialDevelopmentCreateForm(forms.ModelForm):
    class Meta:
        model = SocialDevelopment
        fields = ('country', 'poverty_rate', 'public_health_index', 'education_index',)
        labels = {
            'country':'Kraj', 
            'poverty_rate':'Wskaźnik zagrożenia',
            'public_health_index':'Indeks zdrowia publicznego',
            'education_index':'Indeks edukacji',
        }
        widgets = {
            'country':forms.Select(attrs={
                'class':'form-control'
                }), 
            'poverty_rate':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'public_health_index':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'education_index':forms.NumberInput(attrs={
                'class':'form-control'
                }),
        }