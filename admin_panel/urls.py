from django.urls import path, include
from .views import AgeCreateView, AgeAllView

urlpatterns = [
    path('age_create/', AgeCreateView.as_view(), name='crate_age'),
    path('age_all/', AgeAllView.as_view(), name='all_ages'),
    
]
