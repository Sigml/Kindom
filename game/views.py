from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from datetime import timedelta, date, datetime
import json
from django.http import JsonResponse
from django.contrib import messages
from admin_panel.models import (Country, Age,Resources, Factory, BuildFactory, RequiredResources, Ecology, Trade,
                   Alliance, TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment, CountryResource)
from user.models import CustomUser
from .models import NewWorld, NewWorldResource, NewWorldFactory
from .forms import NewWorldForm
from django.http import HttpResponse



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

            country_resources = CountryResource.objects.filter(country=country)
            for country_resource in country_resources:
                resource=country_resource.resource
                quantity=country_resource.quantity
                
                NewWorldResource.objects.create(
                    new_world=new_world,
                    resource=resource,
                    quantity=quantity
                )

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

            technologies = Technology.objects.all()
            new_world.technologies.set(technologies)

            new_world.save()
            
            print(existing_ecology)


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
        
        in_game = NewWorld.objects.filter(user=request.user).select_related('country')
        
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
            NewWorld.objects.prefetch_related('country', 'age', 'resources', 'ecology', 'technologies'),
            user=request.user, pk=pk
        )

        backpack = NewWorldResource.objects.filter(
            new_world=game,  
        )
        technology = game.technologies.filter(age=game.age)
        resources = game.resources.all()
        resources_dict = {res.resource.image.url: res.quantity for res in backpack}
        ecology = game.ecology.first() if game.ecology.exists() else None
        
        
        if ecology:
            ecology_bars = {
                'air_quality': float(ecology.air_quality) * 10,  
                'water_pollution': float(ecology.water_pollution) * 10,
                'forest_coverage': float(ecology.forest_coverage) * 10,
                'wildlife_population': float(ecology.wildlife_population) * 10,
                'air_quality_empty': 100 - float(ecology.air_quality) * 10,
                'water_pollution_empty': 100 - float(ecology.water_pollution) * 10,
                'forest_coverage_empty': 100 - float(ecology.forest_coverage) * 10,
                'wildlife_population_empty': 100 - float(ecology.wildlife_population) * 10,
            }
        else:
            ecology_bars = None

        if not game.time or game.time.date() < game.age.start_of_era:
            game.time = datetime.combine(game.age.start_of_era, datetime.min.time())
        elif game.time.date() < game.age.end_of_era:
            game.time += timedelta(days=1)
            if game.time.date() > game.age.end_of_era:
                game.time = datetime.combine(game.age.end_of_era, datetime.min.time())

        game.save()
        
        for tech in technology:
            if tech.prerequisite:
                prerequisite_tech = game.technologies.filter(name=tech.prerequisite).first()
                tech.prerequisite_vailable = prerequisite_tech.vailable if prerequisite_tech else False
            else:
                tech.prerequisite_vailable = False
            
            sufficient_resources = True

            if tech.resource_1 and tech.quantity_1:
                resource_1_image = tech.resource_1.image
                if not resources_dict.get(resource_1_image) or resources_dict.get(resource_1_image) < tech.quantity_1:
                    sufficient_resources = False
                    
            if tech.resource_2 and tech.quantity_2:
                resource_2_image = tech.resource_2.image
                if not resources_dict.get(resource_2_image) or resources_dict.get(resource_2_image) < tech.quantity_2:
                    sufficient_resources = False

            if tech.resource_3 and tech.quantity_3:
                resource_3_image = tech.resource_3.image
                if not resources_dict.get(resource_3_image) or resources_dict.get(resource_3_image) < tech.quantity_3:
                    sufficient_resources = False

            tech.sufficient_resources = sufficient_resources
            
        context = {
            'game': game,
            'game_id': game.pk, 
            'time': game.time.strftime('%d-%m-%Y'),
            'resources': resources,
            'resources_dict': resources_dict,
            'backpack': backpack,
            'backpack_resources': backpack,
            'ecology': ecology, 
            'ecology_bars': ecology_bars,
            'technologies':technology
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


def unlock_technology(request, pk, technology_pk):
    game = get_object_or_404(NewWorld, pk=pk)
    technology_to_unlock = get_object_or_404(Technology, pk=technology_pk)


    if technology_to_unlock.age != game.age:
        messages.error(request, "Nie można odblokować tej technologii w tej erze.")
        return redirect('in_game', pk=pk)

    required_resources = [
        (technology_to_unlock.resource_1, technology_to_unlock.quantity_1),
        (technology_to_unlock.resource_2, technology_to_unlock.quantity_2),
        (technology_to_unlock.resource_3, technology_to_unlock.quantity_3),
    ]

    for resource, quantity in required_resources:
        if resource and quantity:
            if not NewWorldResource.objects.filter(new_world=game, resource=resource, quantity__gte=quantity).exists():
                messages.error(request, "Brakuje zasobów do odblokowania technologii.")
                return redirect('in_game', pk=pk)
            
    for resource, quantity in required_resources:
        if resource and quantity:
            resource_to_update = NewWorldResource.objects.get(new_world=game, resource=resource)
            resource_to_update.quantity -= quantity
            resource_to_update.save()

    messages.success(request, f"Technologia {technology_to_unlock.name} została odblokowana.")
    technology_to_unlock.vailable = True
    technology_to_unlock.save()
    game.technologies.add(technology_to_unlock)
    game.save()

    return redirect('in_game', pk=pk)

def update_technology_countdown(request, pk, technology_pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    game = get_object_or_404(NewWorld, pk=pk)
    technology = get_object_or_404(Technology, pk=technology_pk)

    if technology.time_to_unlock:
        technology.time_to_unlock -= 1
        technology.save()

    print(f"Technology name: {technology.name}, Time to unlock: {technology.time_to_unlock}")

    return JsonResponse({
        "time_left": technology.time_to_unlock,
        "is_unlocking": True,
    })
        
    # percentage = (elapsed_duration/total_duration) * 100  if total_duration > 0 else 0
    



