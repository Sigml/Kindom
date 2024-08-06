from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import json
from django.http import JsonResponse
from admin_panel.models import (Country, Age,Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)
from user.models import CustomUser
from .models import NewWorld



class New_World_Create_View(View):
    def get(self, request):
        all_countries = Country.objects.all()
        all_age = Age.objects.all()
        context = {
            'all_countries':all_countries,
            'all_age':all_age, 
        } 
        if not request.user.is_authenticated:
            login_url = f"{reverse_lazy('login')}?next={reverse_lazy('create_new_world')}"
            return redirect(login_url)
        else:
            return render (request, 'new_world.html', context)
        
    
    