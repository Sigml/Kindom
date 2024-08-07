from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import json
from django.http import JsonResponse
from admin_panel.models import (Country, Age,Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)
from user.models import CustomUser
from .models import NewWorld
from .forms import NewWorldForm



class NewWorldCreateView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            login_url = f"{reverse_lazy('login')}?next={reverse_lazy('create_new_world')}"
            return redirect(login_url)
        
        all_countries = Country.objects.all()
        all_age = Age.objects.all()
        context = {
            'all_countries': all_countries,
            'all_age': all_age,
        }
        return render(request, 'new_world.html', context)

    def post(self, request):
        if not request.user.is_authenticated:
            login_url = f"{reverse_lazy('login')}?next={reverse_lazy('create_new_world')}"
            return redirect(login_url)
        
        form = NewWorldForm(request.POST)
        if form.is_valid():
            new_world = form.save(commit=False)
            new_world.user = request.user
            new_world.save()
            form.save_m2m() 
            return redirect('game')
        else:
            print("Błędy formularza:", form.errors)
        
        all_countries = Country.objects.all()
        all_age = Age.objects.all()
        context = {
            'all_countries': all_countries,
            'all_age': all_age,
            'form': form,
            'error': 'Proszę uzupełnić wszystkie wymagane pola.' 
        }
        return render(request, 'new_world.html', context)
        
            
class InGameView(View):
    def get(self, request):
        return render(request, 'game.html',)