from django.db import models

class Age(models.Model):
    name = models.CharField(max_length=64)
    start_of_era = models.DateField(null=True, blank=True)
    end_of_era = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    capital = models.CharField(max_length=64)
    population = models.IntegerField()
    income = models.IntegerField()
    
    def __str__(self):
        return self.name
    

def get_default_country():
    return Country.objects.first()

class Resources(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='resources', default=get_default_country)
    name = models.CharField(max_length=64)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
def factory_image_upload_path(instance, filename):
    return f'factories/{instance.name}/{filename}'
    
class Factory(models.Model):
    name  = models.CharField(max_length=64)
    image = models.ImageField(upload_to= factory_image_upload_path, null=True)
    
    def __str__(self):
        return self.name
    
class RequiredResources(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_resources')
    required_resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='required_for_resources')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.resource.name} wymagany {self.quantity} dla produkcji {self.required_resource.name}"

class BuildFactory(models.Model):
    factory = models.OneToOneField(Factory, on_delete=models.CASCADE, related_name='build_factory')
    age = models.ForeignKey('Age', on_delete=models.CASCADE)
    resources_production = models.ForeignKey(RequiredResources, on_delete=models.CASCADE, null=True)
    required_resource_1 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_1', default=0)
    quantity_required_resource_1 = models.IntegerField(default=1)
    required_resource_2 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_2', default=0)
    quantity_required_resource_2 = models.IntegerField(default=1)
    required_resource_3 = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='build_factory_resource_3', default=0)
    quantity_required_resource_3 = models.IntegerField(default=1)
    
    def __str__(self):
        return self.factory.name
    

class Ecology(models.Model):
    country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='ecology')
    air_quality = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    water_pollution = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    forest_coverage = models.DecimalField(max_digits=10, decimal_places=2, default=10.0)  
    wildlife_population = models.DecimalField(max_digits=10, decimal_places=2, default=10.0) 

    def __str__(self):
        return f"Ekologia - {self.country.name}"
    
class Trade(models.Model):
    exporter = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='exports')
    imports = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='imports')
    resource = models.ForeignKey('Resources', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    
    def __str__(self):
        return f'Państwo {self.exporter.name} impotuje z {self.imports.name} zasob {self.resource.name} ccena {self.price}'
    
    
class Alliance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_1 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='alliance_member_1', default=1)
    member_2 = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='alliance_member_2', default=2)

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
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='army')
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    power = models.IntegerField()
    
class War(models.Model):
    attacker = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='wars_started')
    defender = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='wars_defended')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('ongoing', 'Trwająca'), ('ended', 'Zakończona')], default='ongoing')
    
class Technology(models.Model):
    age = models.ForeignKey(Age, on_delete=models.CASCADE, related_name='age')
    name = models.CharField(max_length=100, unique=True)
    efficiency_production = models.FloatField(default=1.0)
    efficiency_trade = models.FloatField(default=1.0)
    efficiency_military = models.FloatField(default=1.0)
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    impact_economy = models.FloatField(default=0.0)
    impact_society = models.FloatField(default=0.0)
    impact_military = models.FloatField(default=0.0)
    
class SocialDevelopment(models.Model):
    country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='social_development')
    poverty_rate = models.FloatField(default=0.0)
    public_health_index = models.FloatField(default=0.0)
    education_index = models.FloatField(default=0.0)
    