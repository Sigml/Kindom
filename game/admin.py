from django.contrib import admin
from .models import NewWorld

class NewWorldAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'country', 'age', 'list_resources', 'factory', 'list_build_factories', 
        'ecology', 'trade', 'alliance', 'trade_agreement', 'peace_treaty', 
        'army', 'war', 'technology', 'event', 'social_development'
    )
    search_fields = (
        'user__username', 'country__name', 'age__name', 'resources__name',
        'factory__name', 'build_factory__factory__name', 'ecology__country__name',
        'trade__exporter__name', 'alliance__name', 'trade_agreement__alliance__name',
        'peace_treaty__country1__name', 'army__name', 'war__attacker__name',
        'technology__name', 'event__name', 'social_development__name'
    )


admin.site.register(NewWorld, NewWorldAdmin)

