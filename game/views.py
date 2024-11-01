from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from datetime import timedelta, date, datetime
import json
from django.http import JsonResponse
from admin_panel.models import (Country, Age,Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment)
from user.models import CustomUser
from .models import NewWorld, Backpack, BackpackResource
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
            new_world.resources.set(resources) 
            backpack, create = Backpack.objects.get_or_create(user=request.user, country=country)

            for resource in resources:
                backpack_resources, create = BackpackResource.objects.get_or_create(
                    backpack=backpack,
                    resource=resource,
                    defaults={'quantity':1000}
                )

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
            backpack_resources = BackpackResource.objects.filter(backpack=backpack)
            for br in backpack_resources:
                print(f'plecak: {br.resource.name} - {br.quantity}')
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
        backpack = Backpack.objects.get(user=request.user, country=game.country)
        resources = game.resources.all()
        backpack_resources= BackpackResource.objects.filter(backpack=backpack)
        
        
        if not game.time or game.time.date() < game.age.start_of_era:
            game.time = datetime.combine(game.age.start_of_era, datetime.min.time())
        elif game.time.date() < game.age.end_of_era:
            game.time += timedelta(days=1)
            if game.time.date() > game.age.end_of_era:
                game.time = datetime.combine(game.age.end_of_era, datetime.min.time())

        game.save()
            
        
        context = {
            'game':game,
            'time':game.time.strftime('%d-%m-%Y'),
            'resources': resources,
            'backpack':backpack,
            'backpack_resources': backpack_resources
        }
        return render (request, 'in_game.html', context)
    
    
def update_game_day(request, pk):
    game = get_object_or_404(NewWorld, pk=pk)
    game.time += timedelta(days=1)
    
    current_date = game.time.date()
    start_date = game.age.start_of_era
    end_date = game.age.end_of_era
    
    total_duration = (end_date - start_date).days
    elapsed_duration = (current_date - start_date).days
    percentage = (elapsed_duration/total_duration) * 100  if total_duration > 0 else 0
   
    game.save()
    
    new_time = game.time.strftime('%d-%m-%Y')  
    
    return JsonResponse({"new_time": new_time,  "percentage": percentage})