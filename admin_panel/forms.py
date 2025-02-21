from django import forms
from .models import (Age, Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment,
                   CountryResource)


class AgeCreateForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = ('name', 'start_of_era', 'end_of_era', 'image', 'background')
        labels = {
            'name': 'Nazwa epoki',
            'start_of_era': 'Data początku epoki',
            'end_of_era': 'Data końca epoki',
            'image': 'Obraz epoki',
            'background': 'mapa gry'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa epoki'
            }),
            'start_of_era': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'end_of_era':  forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            
        }
        

class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'capital', 'population', 'income', 'image',)
        labels = {
            'name': 'Nazwa kraju',
            'capital': 'Kapitał',
            'population': 'Ilość mieskanców',
            'income': 'Dochód',
            'image': 'Obraz państwa'
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
        fields = ('name', 'price', 'image',)
        labels = {
            'name': 'Nazwa zasobu',
            'price': 'Cena',
            'image': 'Obraz zasobu',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwa zasobu'
                }),
            'price':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Cena'
                }),
        }
        
        
class CountryResourceCreateForm(forms.Form):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(), 
        label='Państwo', widget=forms.Select(attrs={'class':'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        resources= Resources.objects.all()
        for resource in resources:
            self.fields[f"quantity_{resource.id}"] = forms.IntegerField(
                label=f"Ilość dla {resource.name}",
                required=False,
                widget=forms.NumberInput(attrs={'class':'form-control'})
            )
            
        
class CountryResourceUpdateForm(forms.Form):
    quantity = forms.IntegerField(
        label="Ilość",
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )




class FactoryCreateForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ('name', 'image', 'resource', 'quantity', 'technology')
        labels = {
            'name':'Nazwa fabryki',
            'image':'Obrazek fabryki',
            'resource':'Wydobuwajacy zasob',
            'quantity':'ilosc dziennie',
            'technology':'wymagana technologia'
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
        fields = ('resource', 'required_resource', 'quantity', 'image',)
        labels = {
            'resource':'Zasób',
            'required_resource':'Wymagany zasób',
            'quantity':'ILość',
            'image': 'Obraz zasobu',
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
        

class TradeCreateForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ('exporter', 'imports', 'resource', 'price')
        labels = {
            'exporter':'eksporter',
            'imports':'importer',
            'resource':'zasób',
            'price':'Cena'
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
            'price':forms.NumberInput(attrs={
                'class':'form-control'
            }),
        }
        

class AllianceCreateForm (forms.ModelForm):
    class Meta:
        model = Alliance
        fields = ('name', 'member_1', 'member_2',)
        labels = {
                'name':'Nazwa',
                'member_1':'Członek souszu nr_1',
                'member_2':'Członek souszu nr_2'
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'member_1':forms.Select(attrs={
                'class':'form-control'
                }),
                'member_2':forms.Select(attrs={
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
            'participants': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control'
            }),
            'start_date':forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
            'end_date':forms.DateInput(attrs={
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
        fields = ('country', 'name', 'quantity', 'power', 'defense', 'required_resources_1', 'quantity_1', 
                  'required_resources_2', 'quantity_2', 'required_resources_3', 'quantity_3', 'image',)
        labels = {
            'country':'Państwo',
            'name': 'Nazwa wojska',
            'quantity':'Ilość', 
            'power':'Moc',
            'defense':'Obrona',
            'required_resources_1':'Zasob do stworzenia',
            'quantity_1':'Iloćś', 
            'required_resources_2':'Zasob do stworzenia', 
            'quantity_2':'Iloćś', 
            'required_resources_3':'Zasob do stworzenia', 
            'quantity_3':'Iloćś',
            'image':'Obraz wojska',
        }
        widgets = {
            'country':forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control'
            }), 
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'quantity':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'power':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'defense': forms.NumberInput(attrs={
                'class': 'form-control'
                }),
            'required_resources_1':forms.Select(attrs={
                'class': 'form-control'
                }),
            'quantity_1':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'required_resources_2':forms.Select(attrs={
                'class': 'form-control'
                }),
            'quantity_2':forms.NumberInput(attrs={
                'class':'form-control'
                }),
            'required_resources_3':forms.Select(attrs={
                'class': 'form-control'
            }),
            'quantity_3':forms.NumberInput(attrs={
                'class':'form-control'
                }),
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
            'status':'Stan',
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
            'status':forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        
class TechnologyCreateForm (forms.ModelForm):
    resource_1 = forms.ModelChoiceField(queryset=Resources.objects.all(), label='Zasób 1', widget=forms.Select(attrs={'class':'form-control'}))
    quantity_1 = forms.IntegerField(label='Ilość zasobu 1', widget=forms.NumberInput(attrs={'class':'form-control'}))
    resource_2 = forms.ModelChoiceField(queryset=Resources.objects.all(), label='Zasób 2', widget=forms.Select(attrs={'class':'form-control'}))
    quantity_2 = forms.IntegerField(label='Ilość zasobu 2', widget=forms.NumberInput(attrs={'class':'form-control'}))
    resource_3 = forms.ModelChoiceField(queryset=Resources.objects.all(), label='Zasób 3', widget=forms.Select(attrs={'class':'form-control'}))
    quantity_3 = forms.IntegerField(label='Ilość zasobu 3', widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Technology
        fields = ('age', 'name', 'efficiency_production', 'efficiency_trade', 'efficiency_military', 'image', 'prerequisite','description')
        labels = {
            'age':'Epoka',
            'name':'Nazwa', 
            'efficiency_production':'Efektywność produkcji',
            'efficiency_trade':'Efektywność handlu',
            'efficiency_military':'Efektywność wojskowa',
            'image': 'Obraz technologii',
            'prerequisite':'wymagana technologia',
            'description':'Opis',
            
        }
        widgets = {
            'age': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'efficiency_production': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'efficiency_trade': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'efficiency_military': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        
class TechnologyCreateForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('age', 'name', 'efficiency_production', 'efficiency_trade', 'efficiency_military', 'image', 'prerequisite', 'description',
                  'time_to_unlock', 'resource_1', 'quantity_1', 'resource_2', 'quantity_2', 'resource_3', 'quantity_3', 'type', )
        labels = {
            'age': 'Epoka',
            'name': 'Nazwa',
            'efficiency_production': 'Efektywność produkcji',
            'efficiency_trade': 'Efektywność handlu',
            'efficiency_military': 'Efektywność wojskowa',
            'image': 'Obraz technologii',
            'prerequisite': 'wymagana technologia',
            'description': 'Opis',
            'time_to_unlock': 'Czas odblokowania(dni)',
            'resource_1': 'Zasób 1',
            'quantity_1': 'Ilość zasobu 1',
            'resource_2': 'Zasób 2',
            'quantity_2': 'Ilość zasobu 2',
            'resource_3': 'Zasób 3',
            'quantity_3': 'Ilość zasobu 3',
            'type': 'Typ technologii',
        }
        widgets = {
            'age': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'efficiency_production': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'efficiency_trade': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'efficiency_military': forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'time_to_unlock': forms.NumberInput(attrs={'class': 'form-control'}),
            'resource_1': forms.Select(attrs={'class': 'form-control'}),
            'quantyty_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'resource_2': forms.Select(attrs={'class': 'form-control'}),
            'quantity_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'resource_3': forms.Select(attrs={'class': 'form-control'}),
            'quantity_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

    

            
            
class EventCreateForm (forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'impact_economy', 'impact_society', 'impact_military', 'image',)
        labels = {
            'name':'Nazwa',
            'description':'Opis',
            'impact_economy':'Wpływ gospodarczy', 
            'impact_society':'Wpływ społeczeństwa',
            'impact_military':'Wpływ wojskowy',
            'image':"Obraz wydarżenia",
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'description':forms.TextInput(attrs={
                'class':'form-control'
                }),
            'impact_economy':forms.NumberInput(attrs={
                'class':'form-control', 
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
        fields = ('name', 'poverty_rate', 'public_health_index', 'education_index', 'image',)
        labels = {
            'name':'Nazwa',
            'poverty_rate':'Wskaźnik zagrożenia',
            'public_health_index':'Indeks zdrowia publicznego',
            'education_index':'Indeks edukacji',
            'image': ' Obraz',
        }
        widgets = {
            'name':forms.TextInput(attrs={
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
        
