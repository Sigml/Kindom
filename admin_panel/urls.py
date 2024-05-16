from django.urls import path, include
from .views import (AgeCreateView, AgeListView, AgeUpdateView, AgeDeleteView, CountryCreateView, CountryListView, 
                    CountryUpdateView)

urlpatterns = [
    path('age_create/', AgeCreateView.as_view(), name='crate_age'),
    path('age_all/', AgeListView.as_view(), name='all_ages'),
    path('age_update/<pk>/', AgeUpdateView.as_view(), name='age_update'),
    path('age_delete/<pk>/', AgeDeleteView.as_view(), name='age_delete'),
    path('country_create/', CountryCreateView.as_view(), name='country_create'),
    path('country_list/', CountryListView.as_view(), name='country_list'),
    path('country_update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    
]
