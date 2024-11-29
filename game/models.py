from django.db import models
from datetime import datetime

from user.models import CustomUser
from admin_panel.models import (Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment, Age, 
                   CountryResource)

class NewWorld(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='worlds')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='worlds')
    age = models.ForeignKey(Age, on_delete=models.CASCADE, related_name='worlds')
    resources = models.ManyToManyField(Resources, through='NewWorldResource', related_name='worlds', blank=True)
    time = models.DateTimeField(default=datetime(1, 1, 1))
    factories = models.ManyToManyField(Factory, through='NewWorldFactory', related_name='worlds', blank=True)
    build_factories = models.ManyToManyField(BuildFactory, related_name='worlds', blank=True)
    required_resources = models.ManyToManyField(RequiredResources, related_name='worlds', blank=True)
    ecology = models.ManyToManyField(Ecology, related_name='worlds', blank=True)
    trade = models.OneToOneField(Trade, on_delete=models.CASCADE, related_name='worlds', null=True, blank=True)
    alliances = models.ManyToManyField(Alliance, related_name='worlds', blank=True)
    trade_agreements = models.ManyToManyField(TradeAgreement, related_name='worlds', blank=True)
    peace_treaties = models.ManyToManyField(PeaceTreaty, related_name='worlds', blank=True)
    armies = models.ManyToManyField(Army, related_name='worlds', blank=True)
    wars = models.ManyToManyField(War, related_name='worlds', blank=True)
    technologies = models.ManyToManyField(Technology, related_name='worlds', blank=True)
    events = models.ManyToManyField(Event, related_name='worlds', blank=True)
    social_development = models.OneToOneField(SocialDevelopment, on_delete=models.CASCADE, related_name='worlds', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.country.name} - {self.age.name}"

    def list_resources(self):
        return ", ".join([f"{nw.resource.name} ({nw.quantity})" for nw in self.newworldresource_set.all()])

    list_resources.short_description = "Zasoby"

    def list_factories(self):
        return ", ".join([f"{nw.factory.name} ({nw.quantity})" for nw in self.newworldfactory_set.all()])

    list_factories.short_description = "Fabryki"


class NewWorldResource(models.Model):
    new_world = models.ForeignKey(NewWorld, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.resource.name} ({self.quantity}) dla {self.new_world.country.name}"


class NewWorldFactory(models.Model):
    new_world = models.ForeignKey(NewWorld, on_delete=models.CASCADE)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.factory.name} ({self.quantity}) dla {self.new_world.country.name}"
