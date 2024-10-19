from django.db import models
from datetime import datetime

from user.models import CustomUser
from admin_panel.models import (Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment, Age)

class NewWorld(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_world')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country')
    age = models.ForeignKey(Age, on_delete=models.CASCADE, related_name='user_age')
    resources = models.ManyToManyField(Resources, related_name='world_resources', blank=True)
    time = models.DateTimeField(default=datetime(1,1,1))
    factory = models.OneToOneField(Factory, on_delete=models.CASCADE, related_name='world_factory', null=True, blank=True)
    build_factory = models.ManyToManyField(BuildFactory, related_name='world_build_factories', blank=True)
    required_resources = models.ManyToManyField(RequiredResources, related_name='world_required_resources', blank=True)
    ecology = models.OneToOneField(Ecology, on_delete=models.CASCADE, related_name='world_ecology', null=True, blank=True)
    trade = models.OneToOneField(Trade, on_delete=models.CASCADE, related_name='world_trade', null=True, blank=True)
    alliance = models.OneToOneField(Alliance, on_delete=models.CASCADE, related_name='world_alliance', null=True, blank=True)
    trade_agreement = models.OneToOneField(TradeAgreement, on_delete=models.CASCADE, related_name='world_trade_agreement', null=True, blank=True)
    peace_treaty = models.OneToOneField(PeaceTreaty, on_delete=models.CASCADE, related_name='world_peace_treaty', null=True, blank=True)
    army = models.OneToOneField(Army, on_delete=models.CASCADE, related_name='world_army', null=True, blank=True)
    war = models.OneToOneField(War, on_delete=models.CASCADE, related_name='world_war', null=True, blank=True)
    technology = models.OneToOneField(Technology, on_delete=models.CASCADE, related_name='world_technology', null=True, blank=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='world_event', null=True, blank=True)
    social_development = models.OneToOneField(SocialDevelopment, on_delete=models.CASCADE, related_name='world_social_development', null=True, blank=True)

    def __str__(self):
        return self.country.name
    
    def list_resources(self):
        return ", ".join([resource.name for resource in self.resources.all()])

    list_resources.short_description = "Zasoby"

    def list_build_factories(self):
        return ", ".join([factory.name for factory in self.build_factory.all()])

    list_build_factories.short_description = "Wybudowane fabryki"
    

class Backpack(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='backpacks')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='backpacks')
    resources = models.ManyToManyField(Resources, through='BackpackResource', related_name='backpacks')
    # required_resources = models.ManyToManyField(RequiredResources, through='BackpackResource', related_name='backpacks')

    def __str__(self):
        return f"Plecak dla {self.user.username}"

class BackpackResource(models.Model):
    backpack = models.ForeignKey(Backpack, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    # required_resources = models.ForeignKey(RequiredResources, on_delete=models.CASCADE)
    # quantity_required_resources = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} dla {self.resource.name} w {self.backpack.user.username} plecaku"
