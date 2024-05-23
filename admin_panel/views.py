from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView
from game.models import (Age, Country, Resources, Factory, RequiredResources, BuildFactory) 
from .forms import (AgeCreateForm, CountryCreateForm, ResourcesCreateForm, FactoryCreateForm, RequiredResourcesCreateForm,
                    BuildFactoryCreateForm)


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