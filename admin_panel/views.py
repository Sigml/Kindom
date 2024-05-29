from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView
from game.models import (Age, Country, Resources, Factory, RequiredResources, BuildFactory, Ecology, Trade, Alliance,
                         TradeAgreement, PeaceTreaty, Army, War, Technology, Event, SocialDevelopment) 
from .forms import (AgeCreateForm, CountryCreateForm, ResourcesCreateForm, FactoryCreateForm, RequiredResourcesCreateForm,
                    BuildFactoryCreateForm, EcologyCreateForm, TradeCreateForm, AllianceCreateForm, TradeAgreementCreateForm,
                    PeaceTreatyCreateForm, ArmyCreateForm, WarCreateForm, TechnologyCreateForm, EventCreateForm, SocialDevelopmentCreateForm)


def main(request):
    return render(request, 'base.html')


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class AgeCreateView(AdminRequiredMixin, CreateView):
    model = Age
    form_class = AgeCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('all_ages')
    

class AgeListView(AdminRequiredMixin, View):
    def get(self, request):
        age_all = Age.objects.all()
        context = {
            'age_all': age_all
        }
        return render(request, 'age_all.html', context)
    

class AgeUpdateView(AdminRequiredMixin, UpdateView):
    model = Age
    template_name = 'forms.html'
    form_class = AgeCreateForm
    success_url = reverse_lazy('all_ages')
    

class AgeDeleteView(AdminRequiredMixin, DeleteView):
    model = Age
    template_name = 'delete.html'
    success_url = reverse_lazy('all_ages')

    
class CountryCreateView(AdminRequiredMixin, CreateView):
    model = Country
    form_class = CountryCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('country_list')
    

class CountryListView(AdminRequiredMixin, ListView):
    model = Country
    template_name = 'country_list.html'
    
    def get_queruset(self, *agrs, **kwargs):
        qs = super().get_queruset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    

class CountryUpdateView(AdminRequiredMixin, UpdateView):
    model = Country
    template_name = 'forms.html'
    form_class = CountryCreateForm
    success_url = reverse_lazy('country_list')
    
    
class CountryDeleteView(AdminRequiredMixin, DeleteView):
    model = Country
    template_name = 'delete.html'
    success_url = reverse_lazy('country_list')


class ResourcesCreateView(AdminRequiredMixin, CreateView):
    model = Resources
    form_class = ResourcesCreateForm
    template_name = 'forms.html'
    success_url = reverse_lazy('resources_list')
    

class ResourcesListView(AdminRequiredMixin, ListView):
    model = Resources
    template_name = 'resources_list.html'
    
    def get_queruset(self, *agrs, **kwargs):
        qs = super().get_queruset(*agrs, **kwargs)
        qs = qs.order_by('-country')
        return qs
    

class ResourcesUpdateView(AdminRequiredMixin, UpdateView):
    model = Resources
    template_name = 'forms.html'
    form_class = ResourcesCreateForm
    success_url = reverse_lazy('resources_list')
    
    
class ResourcesDeleteView(AdminRequiredMixin, DeleteView):
    model = Resources
    template_name = 'delete.html'
    success_url = reverse_lazy('resources_list')


class FactoryCreateView(AdminRequiredMixin, CreateView):
    model = Factory
    template_name = 'forms.html'
    form_class = FactoryCreateForm
    success_url = reverse_lazy('factory_list')
    
    
class FactoryListView(AdminRequiredMixin, ListView):
    model = Factory
    template_name = 'factory_list.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class FactoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Factory
    template_name = 'forms.html'
    form_class = FactoryCreateForm
    success_url = reverse_lazy('factory_list')
    

class FactoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Factory
    template_name = 'delete.html'
    success_url = reverse_lazy('factory_list')
    

class RequiredResourcesCreateView(AdminRequiredMixin, CreateView):
    model = RequiredResources
    template_name = 'forms.html'
    form_class = RequiredResourcesCreateForm
    success_url = reverse_lazy('required_resources_list')
    
    
class RequiredResourcesListView(AdminRequiredMixin, ListView):
    model = RequiredResources
    template_name = 'required_resources_list.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class RequiredResourcesUpdateView(AdminRequiredMixin, UpdateView):
    model = RequiredResources
    template_name = 'forms.html'
    form_class = RequiredResourcesCreateForm
    success_url = reverse_lazy('required_resources_list')
    

class RequiredResourcesDeleteView(AdminRequiredMixin, DeleteView):
    model = RequiredResources
    template_name = 'delete.html'
    success_url = reverse_lazy('required_resources_list')
    
    
class BuildFactoryCreateView(AdminRequiredMixin, CreateView):
    model = BuildFactory
    template_name = 'forms.html'
    form_class = BuildFactoryCreateForm
    success_url = reverse_lazy('build_factory_list')
    
    
class BuildFactoryListView(AdminRequiredMixin, ListView):
    model = BuildFactory
    template_name = 'build_factory_list.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class BuildFactoryUpdateView(AdminRequiredMixin, UpdateView):
    model = BuildFactory
    template_name = 'forms.html'
    form_class = BuildFactoryCreateForm
    success_url = reverse_lazy('build_factory_list')
    

class BuildFactoryDeleteView(AdminRequiredMixin, DeleteView):
    model = BuildFactory
    template_name = 'delete.html'
    success_url = reverse_lazy('build_factory_list')
    

class EcologyCreateView(AdminRequiredMixin, CreateView):
    model = Ecology
    template_name = 'forms.html'
    form_class = EcologyCreateForm
    success_url = reverse_lazy('ecology_list')
    
    
class EcologyListView(AdminRequiredMixin, ListView):
    model = Ecology
    template_name = 'ecology_list.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class EcologyUpdateView(AdminRequiredMixin, UpdateView):
    model = Ecology
    template_name = 'forms.html'
    form_class = EcologyCreateForm
    success_url = reverse_lazy('ecology_list')
    

class EcologyDeleteView(AdminRequiredMixin, DeleteView):
    model = Ecology
    template_name = 'delete.html'
    success_url = reverse_lazy('ecology_list')
    
    
class TradeCreateView(AdminRequiredMixin, CreateView):
    model = TradeAgreement
    template_name = 'forms.html'
    form_class = TradeAgreementCreateForm
    success_url = reverse_lazy('trade_list')
    
    
class TradeListView(AdminRequiredMixin, ListView):
    model = Trade
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class TradeUpdateView(AdminRequiredMixin, UpdateView):
    model = Trade
    template_name = 'forms.html'
    form_class = TradeAgreementCreateForm
    success_url = reverse_lazy('trade_list')
    

class TradeDeleteView(AdminRequiredMixin, DeleteView):
    model = Trade
    template_name = 'delete.html'
    success_url = reverse_lazy('trade_list')
    
    
class AllianceCreateView(AdminRequiredMixin, CreateView):
    model = Alliance
    template_name = 'forms.html'
    form_class = AllianceCreateForm
    success_url = reverse_lazy('alliance_list')
    
    
class AllianceListView(AdminRequiredMixin, ListView):
    model = Alliance
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class AllianceUpdateView(AdminRequiredMixin, UpdateView):
    model = Alliance
    template_name = 'forms.html'
    form_class = AgeCreateForm
    success_url = reverse_lazy('alliance_list')
    

class AllianceDeleteView(AdminRequiredMixin, DeleteView):
    model = Alliance
    template_name = 'delete.html'
    success_url = reverse_lazy('alliance_list')
    

class TradeAgreementCreateView(AdminRequiredMixin, CreateView):
    model = TradeAgreement
    template_name = 'forms.html'
    form_class = TechnologyCreateForm
    success_url = reverse_lazy('treade_agreement_list')
    
    
class TradeAgreementListView(AdminRequiredMixin, ListView):
    model = TradeAgreement
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class TradeAgreementUpdateView(AdminRequiredMixin, UpdateView):
    model = TradeAgreement
    template_name = 'forms.html'
    form_class = TechnologyCreateForm
    success_url = reverse_lazy('treade_agreement_list')
    

class TradeAgreementDeleteView(AdminRequiredMixin, DeleteView):
    model = TradeAgreement
    template_name = 'delete.html'
    success_url = reverse_lazy('treade_agreement_list')
    

class PeaceTreatyCreateView(AdminRequiredMixin, CreateView):
    model = PeaceTreaty
    template_name = 'forms.html'
    form_class = PeaceTreatyCreateForm
    success_url = reverse_lazy('peace_teatry_list')
    
    
class PeaceTreatyListView(AdminRequiredMixin, ListView):
    model = PeaceTreaty
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class PeaceTreatyUpdateView(AdminRequiredMixin, UpdateView):
    model = PeaceTreaty
    template_name = 'forms.html'
    form_class = PeaceTreatyCreateForm
    success_url = reverse_lazy('peace_teatry_list')
    

class PeaceTreatyDeleteView(AdminRequiredMixin, DeleteView):
    model = PeaceTreaty
    template_name = 'delete.html'
    success_url = reverse_lazy('peace_teatry_list')
    
    
class ArmyCreateView(AdminRequiredMixin, CreateView):
    model = Army
    template_name = 'forms.html'
    form_class = ArmyCreateForm
    success_url = reverse_lazy('army_list')
    
    
class ArmyListView(AdminRequiredMixin, ListView):
    model = Army
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class ArmyUpdateView(AdminRequiredMixin, UpdateView):
    model = Army
    template_name = 'forms.html'
    form_class = ArmyCreateForm
    success_url = reverse_lazy('army_list')
    

class ArmyDeleteView(AdminRequiredMixin, DeleteView):
    model = Army
    template_name = 'delete.html'
    success_url = reverse_lazy('army_list')


class WarCreateView(AdminRequiredMixin, CreateView):
    model = War
    template_name = 'forms.html'
    form_class = WarCreateForm
    success_url = reverse_lazy('war_list')
    
    
class WarListView(AdminRequiredMixin, ListView):
    model = War
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class WarUpdateView(AdminRequiredMixin, UpdateView):
    model = War
    template_name = 'forms.html'
    form_class = WarCreateForm
    success_url = reverse_lazy('war_list')
    

class WarDeleteView(AdminRequiredMixin, DeleteView):
    model = War
    template_name = 'delete.html'
    success_url = reverse_lazy('war_list')


class TechnologyCreateView(AdminRequiredMixin, CreateView):
    model = Technology
    template_name = 'forms.html'
    form_class = TechnologyCreateForm
    success_url = reverse_lazy('technology_list')
    
    
class TechnologyListView(AdminRequiredMixin, ListView):
    model = Technology
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class TechnologyUpdateView(AdminRequiredMixin, UpdateView):
    model = Technology
    template_name = 'forms.html'
    form_class = TechnologyCreateForm
    success_url = reverse_lazy('technology_list')
    

class TechnologyDeleteView(AdminRequiredMixin, DeleteView):
    model = Technology
    template_name = 'delete.html'
    success_url = reverse_lazy('technology_list')


class EventCreateView(AdminRequiredMixin, CreateView):
    model = Event
    template_name = 'forms.html'
    form_class = EventCreateForm
    success_url = reverse_lazy('event_list')
    
    
class EventListView(AdminRequiredMixin, ListView):
    model = Event
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class EventUpdateView(AdminRequiredMixin, UpdateView):
    model = Event
    template_name = 'forms.html'
    form_class = EventCreateForm
    success_url = reverse_lazy('event_list')
    

class EventDeleteView(AdminRequiredMixin, DeleteView):
    model = Event
    template_name = 'delete.html'
    success_url = reverse_lazy('event_list')


class SocialDevelopmentCreateView(AdminRequiredMixin, CreateView):
    model = SocialDevelopment
    template_name = 'forms.html'
    form_class = SocialDevelopmentCreateForm
    success_url = reverse_lazy('social_development_list')
    
    
class SocialDevelopmentListView(AdminRequiredMixin, ListView):
    model = SocialDevelopment
    template_name = '.html'
    
    def get_queryset(self, *agrs, **kwargs):
        qs = super().get_queryset(*agrs, **kwargs)
        qs = qs.order_by('-id')
        return qs
    
    
class SocialDevelopmentUpdateView(AdminRequiredMixin, UpdateView):
    model = SocialDevelopment
    template_name = 'forms.html'
    form_class = SocialDevelopmentCreateForm
    success_url = reverse_lazy('social_development_list')
    

class SocialDevelopmentDeleteView(AdminRequiredMixin, DeleteView):
    model = SocialDevelopment
    template_name = 'delete.html'
    success_url = reverse_lazy('social_development_list')
