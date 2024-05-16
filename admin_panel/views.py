from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, View, ListView, UpdateView, DeleteView
from game.models import Age, Country
from .forms import AgeCreateForm, CountryCreateForm


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
    
    
class AgeDeleteView(AdminRequiredMixin, DeleteView):
    model = Country
    template_name = 'delete.html'
    success_url = reverse_lazy('country_list')

