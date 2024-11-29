from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from datetime import timedelta, date, datetime
import json
from django.http import JsonResponse
from admin_panel.models import (Country, Age,Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment, CountryResource)
from user.models import CustomUser
from .models import NewWorld, NewWorldResource, NewWorldFactory
from .forms import NewWorldForm



from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .forms import NewWorldForm
from .models import Country, Age, Resources, Ecology, BuildFactory, Technology, NewWorld

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
            country = form.cleaned_data['country']  
            age = form.cleaned_data['age'] 

            new_world = NewWorld(user=request.user, country=country, age=age)
            new_world.save()

            resources = [cr.resource for cr in CountryResource.objects.filter(country=country)]
            new_world.resources.set(resources)

            existing_ecology = Ecology.objects.filter(country=country).first()

            if existing_ecology:
                new_world.ecology.set([existing_ecology])
            else:
                new_ecology = Ecology.objects.create(
                    country=country,
                    air_quality=10.0,
                    water_pollution=10.0,
                    forest_coverage=10.0,
                    wildlife_population=10.0
                )
                new_world.ecology.set([new_ecology])

            factories = BuildFactory.objects.filter(age=age)
            new_world.build_factories.set(factories)

            technologies = Technology.objects.filter(age=age)
            if technologies.exists():
                new_world.technologies.add(technologies.first())

            new_world.save()

            print(f"Zasoby dla {new_world.country.name}:")
        # Iteracja po zasobach i wyświetlenie ich ilości
        for resource in resources:
            # Znajdź odpowiedni obiekt NewWorldResource dla zasobu i pobierz jego ilość
            resource_quantity = NewWorldResource.objects.filter(new_world=new_world, resource=resource)
            if resource_quantity:
                print(f"{resource.name}, {resource_quantity.quantity}")
            else:
                print(f"{resource.name}, 0")

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
        game = get_object_or_404(
            NewWorld.objects.prefetch_related('country', 'age', 'resources', 'ecology'),
            user=request.user, pk=pk
        )

        backpack = NewWorldResource.objects.filter(
            new_world=game,  
        )
        

        resources = game.resources.all()

        if not game.time or game.time.date() < game.age.start_of_era:
            game.time = datetime.combine(game.age.start_of_era, datetime.min.time())
        elif game.time.date() < game.age.end_of_era:
            game.time += timedelta(days=1)
            if game.time.date() > game.age.end_of_era:
                game.time = datetime.combine(game.age.end_of_era, datetime.min.time())

        game.save()

        context = {
            'game': game,
            'time': game.time.strftime('%d-%m-%Y'),
            'resources': resources,
            'backpack': backpack,
            'backpack_resources': backpack
        }

        return render(request, 'in_game.html', context)
    
    
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