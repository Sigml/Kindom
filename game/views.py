from django.shortcuts import render
from django.views import View
from admin_panel.models import (Country, Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)
from user.models import CustomUser
from .models import NewWorld



class New_World_Create_View(View):
    def get(self, request):
        all_countries = Country.objects.all()
        context = {
            'all_countries':all_countries,
        }
        return render (request, 'new_world.html', context)
    