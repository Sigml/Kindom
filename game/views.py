from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
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

            country = form.cleaned_data['country']
            new_world.save() 

            resources = Resources.objects.filter(country=country)
            print("Dostępne zasoby:", resources) 
            new_world.resources.set(resources) 
            print("Zasoby przypisane do nowego świata:", new_world.resources.all())

            existing_ecology = Ecology.objects.filter(country=country).first()

            if existing_ecology:
                new_world.ecology = Ecology.objects.create(
                    country=country,
                    air_quality=existing_ecology.air_quality,
                    water_pollution=existing_ecology.water_pollution,
                    forest_coverage=existing_ecology.forest_coverage,
                    wildlife_population=existing_ecology.wildlife_population
                )

            new_world.save() 
            form.save_m2m()  

            return redirect('in_game', pk=new_world.pk)

        all_countries = Country.objects.all()
        all_age = Age.objects.all()
        context = {
            'all_countries': all_countries,
            'all_age': all_age,
            'form': form,
            'error': 'Proszę uzupełnić wszystkie wymagane pola.'
        }
        return render(request, 'new_world.html', context)



    
class SelectGameView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        in_game = NewWorld.objects.filter(user=request.user).select_related('country').prefetch_related('country__resources',)
        
        context = {
            'in_game': in_game
        }
        return render(request, 'select_game.html', context)
    
    
class DeleteGameDeleteView(DeleteView):
    model = NewWorld
    success_url = reverse_lazy('select_game')
    template_name = 'delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse_lazy('select_game')
        return context
    
    
    
    
class InGameView(View):
    def get(self, request, pk):
        game = get_object_or_404(NewWorld.objects.prefetch_related('country', 'age', 'resources', 'ecology'), user=request.user, pk=pk)
        resources = game.resources.all()
        if not game.time or game.time.year == 1:
            game.time = game.age.start_of_era
        else:
            game.time
        
        context = {
            'game':game,
            'time':game.time,
            'resources': resources
        }
        for resource in resources:
            print(f"Zasób przekazywany do kontekstu: Nazwa: {resource.name}, Ilość: {resource.quantity}")
        return render (request, 'in_game.html', context)