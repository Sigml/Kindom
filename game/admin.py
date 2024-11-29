from django.contrib import admin
from .models import NewWorld

class NewWorldAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'country', 'age', 'list_resources', 'list_build_factories',
        'list_ecology', 'list_trade', 'list_alliances', 'list_trade_agreements',
        'list_peace_treaties', 'list_armies', 'list_wars',
        'list_technologies', 'list_events', 'list_social_development'
    )
    search_fields = (
        'user__username', 'country__name', 'age__name', 
        'resources__name', 'factory__name', 'ecology__country__name',
        'trade__exporter__name', 'alliance__name', 
        'peace_treaty__country1__name', 'army__name', 
        'war__attacker__name', 'technology__name', 
        'event__name', 'social_development__name'
    )

    @admin.display(description='Resources')
    def list_resources(self, obj):
        return ", ".join([str(resource.name) for resource in obj.resources.all()])

    @admin.display(description='Build Factories')
    def list_build_factories(self, obj):
        return ", ".join([str(bf.factory.name) for bf in obj.build_factories.all()])

    @admin.display(description='Ecology')
    def list_ecology(self, obj):
        return ", ".join([str(ecology) for ecology in obj.ecology.all()])

    @admin.display(description='Trades')
    def list_trade(self, obj):
        return str(obj.trade) if obj.trade else 'No trade'

    @admin.display(description='Alliances')
    def list_alliances(self, obj):
        return ", ".join([str(alliance) for alliance in obj.alliances.all()])

    @admin.display(description='Trade Agreements')
    def list_trade_agreements(self, obj):
        return ", ".join([str(agreement) for agreement in obj.trade_agreements.all()])

    @admin.display(description='Peace Treaties')
    def list_peace_treaties(self, obj):
        return ", ".join([str(treaty) for treaty in obj.peace_treaties.all()])

    @admin.display(description='Armies')
    def list_armies(self, obj):
        return ", ".join([str(army) for army in obj.armies.all()])

    @admin.display(description='Wars')
    def list_wars(self, obj):
        return ", ".join([str(war) for war in obj.wars.all()])

    @admin.display(description='Technologies')
    def list_technologies(self, obj):
        return ", ".join([str(technology) for technology in obj.technologies.all()])

    @admin.display(description='Events')
    def list_events(self, obj):
        return ", ".join([str(event) for event in obj.events.all()])

    @admin.display(description='Social Development')
    def list_social_development(self, obj):
        return str(obj.social_development) if obj.social_development else 'No development'

admin.site.register(NewWorld, NewWorldAdmin)
