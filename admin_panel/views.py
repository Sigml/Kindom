from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, View
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
    

class AgeAllView(AdminRequiredMixin, View):
    def get(self, request):
        age_all = Age.objects.all()
        context = {
            'age_all': age_all
        }
        return render(request, 'age_all.html', context)
    
    

