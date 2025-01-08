from django.db import models

class Age(models.Model):
    name = models.CharField(max_length=64)
    start_of_era = models.DateField(null=True, blank=True)
    end_of_era = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='age_image/', max_length=255,null=True, blank=True)
    background = models.ImageField(upload_to='background_age_image/',max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    capital = models.CharField(max_length=64)
    population = models.IntegerField()
    income = models.IntegerField()
    image = models.ImageField(upload_to='country_image/', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Resources(models.Model):
    name = models.CharField(max_length=64, unique=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image = models.ImageField(upload_to='resources_image/', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class CountryResource(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_resources')  
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='resources_country') 
    quantity = models.IntegerField(null=True) 
    
    def __str__(self):
        return f"{self.resource.name} - {self.country.name} - {self.quantity}"

class Technology(models.Model):
    age = models.ForeignKey(Age, on_delete=models.CASCADE, related_name='age')
    name = models.CharField(max_length=100, unique=True)
    efficiency_production = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    efficiency_trade = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    efficiency_military = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    image = models.ImageField(upload_to='technology_image', null=True, blank=True)
    prerequisite = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_technologies')
    description = models.TextField(max_length=300, null=True, blank=True)
    resources = models.ManyToManyField(Resources, related_name='resources_to_unlock', blank=True)
    vailable = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    
class Factory(models.Model):
    FACTORY_TYPE_CHOICES = [
        ('MILITARY', 'Wojsko'),          
        ('DEFENSE', 'Obrona'),         
        ('MINING', 'Wydobycie surowców'),
        ('DEVELOPMENT', 'Rozwój'),     
        ('HOUSING', 'Mieszkalnictwo'),  
        ('WONDERS', 'Cudy świata'), 
    ]
    name  = models.CharField(max_length=64)
    image = models.ImageField(upload_to='factory_image/', max_length=255, null=True, blank=True)
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, default=1)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    type = models.CharField(choices=FACTORY_TYPE_CHOICES, max_length=255, default='MILITARY')
    technology = models.ManyToManyField('Technology', related_name='technology', blank=True,)
    
    
    def __str__(self):
        return self.name
    
class RequiredResources(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_resources')
    required_resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_for_resources')
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='required_resources_images/', max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.resource.name} wymagany {self.quantity} dla produkcji {self.required_resource.name}"

class BuildFactory(models.Model):
    factory = models.OneToOneField(Factory, on_delete=models.CASCADE, related_name='build_factory')
    age = models.ForeignKey('Age', on_delete=models.CASCADE)
    resources_production = models.ForeignKey(RequiredResources, on_delete=models.CASCADE, null=True)
    required_resource_1 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_1')
    quantity_required_resource_1 = models.IntegerField()
    required_resource_2 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_2')
    quantity_required_resource_2 = models.IntegerField()
    required_resource_3 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_3')
    quantity_required_resource_3 = models.IntegerField()
    technology = models.ManyToManyField('Technology', related_name='required_technology', blank=True)
    
    
    def __str__(self):
        return self.factory.name
    

class Ecology(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    air_quality = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    image_air_quality = models.ImageField(upload_to='ecology_images/', null=True, blank=True)
    water_pollution = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    image_water_pollution = models.ImageField(upload_to='ecology_images/', null=True, blank=True)
    forest_coverage = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    image_forest_coverage = models.ImageField(upload_to='ecology_images/', null=True, blank=True)
    wildlife_population = models.DecimalField(max_digits=10, decimal_places=2, default=10.0) 
    image_wildlife_population = models.ImageField(upload_to='ecology_images/', null=True, blank=True)
 
    def __str__(self):
        return f"Ekologia - {self.air_quality, self.water_pollution,self.forest_coverage, self.wildlife_population}"
    
class Trade(models.Model):
    exporter = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='exports')
    imports = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='imports')
    resource = models.ForeignKey('Resources', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    
    def __str__(self):
        return f'Państwo {self.exporter.name} impotuje z {self.imports.name} zasob {self.resource.name} ccena {self.price}'
    
    
class Alliance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_1 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='alliance_member_1')
    member_2 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='alliance_member_2')

    def __str__(self):
        return self.name

class TradeAgreement(models.Model):
    alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE, related_name='trade_agreements')
    participants = models.ManyToManyField('Country', related_name='trade_agreements')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Umowa handlowa - {self.alliance.name}"

class PeaceTreaty(models.Model):
    country1 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='peace_treaties_as_country1')
    country2 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='peace_treaties_as_country2')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Traktat pokojowy - {self.country1.name} i {self.country2.name}"

class Army(models.Model):
    country = models.ManyToManyField(Country, related_name='army')
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    power = models.IntegerField()
    defense = models.IntegerField()
    required_resources_1 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_resources_1', null=True)
    quantity_1 = models.IntegerField()
    required_resources_2 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_resources_2', null=True)
    quantity_2 = models.IntegerField()
    required_resources_3 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_resources_3', null=True)
    quantity_3 = models.IntegerField()
    image = models.ImageField(upload_to='army_image/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class War(models.Model):
    attacker = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='wars_started')
    defender = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='wars_defended')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Trwająca'), ('ended', 'Zakończona')], default='ongoing')
    
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    impact_economy = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    impact_society = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    impact_military = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    image = models.ImageField(upload_to='event_image/', null=True, blank=True)
    
class SocialDevelopment(models.Model):
    name = models.CharField(max_length=100, default='wydarzenie')
    poverty_rate = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    public_health_index = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    education_index = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    image = models.ImageField(upload_to='social_development_image/', null=True, blank=True)
    
