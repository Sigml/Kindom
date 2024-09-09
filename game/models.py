from django.db import models

from user.models import CustomUser
from admin_panel.models import (Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment, Age)

class NewWorld(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_world')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='user_country')
    age = models.ForeignKey(Age, on_delete=models.CASCADE, related_name='user_age')
    resources = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='world_resources', null=True, blank=True)
    factory = models.OneToOneField(Factory, on_delete=models.CASCADE, related_name='world_factory', null=True, blank=True)
    build_factory = models.ForeignKey(BuildFactory, on_delete=models.CASCADE, related_name='world_build_factories', null=True, blank=True)
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