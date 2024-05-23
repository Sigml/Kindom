from django.urls import path, include
from .views import (AgeCreateView, AgeListView, AgeUpdateView, AgeDeleteView, CountryCreateView, CountryListView, 
                    CountryUpdateView, CountryDeleteView, ResourcesCreateView, ResourcesListView, ResourcesUpdateView,
                    ResourcesDeleteView, FactoryCreateView, FactoryListView, FactoryUpdateView, FactoryDeleteView,
                    RequiredResourcesCreateView, RequiredResourcesListView, RequiredResourcesUpdateView, RequiredResourcesDeleteView,
                    BuildFactoryCreateView, BuildFactoryListView, BuildFactoryUpdateView, BuildFactoryDeleteView,
                    
                    )

urlpatterns = [
    path('age_create/', AgeCreateView.as_view(), name='crate_age'),
    path('age_list/', AgeListView.as_view(), name='all_ages'),
    path('age_update/<pk>/', AgeUpdateView.as_view(), name='age_update'),
    path('age_delete/<pk>/', AgeDeleteView.as_view(), name='age_delete'),
    path('country_create/', CountryCreateView.as_view(), name='country_create'),
    path('country_list/', CountryListView.as_view(), name='country_list'),
    path('country_update/<pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country_delete/<pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('resources_create/', ResourcesCreateView.as_view(), name='resources_create'),
    path('resources_list/', ResourcesListView.as_view(), name='resources_list'),
    path('resources_update/<pk>/', ResourcesUpdateView.as_view(), name='resources_update'),
    path('resources_delete/<pk>/', ResourcesDeleteView.as_view(), name='resources_delete'),
    path('factory_create/', FactoryCreateView.as_view(), name='factory_create'),
    path('factory_list/', FactoryListView.as_view(), name='factory_list'),
    path('factory_update/<pk>/', FactoryUpdateView.as_view(), name='factory_update'),
    path('factory_delete/<pk>/', FactoryDeleteView.as_view(), name='factory_delete'),
    path('required_resources_create/', RequiredResourcesCreateView.as_view(), name='required_resources_create'),
    path('required_resources_list/', RequiredResourcesListView.as_view(), name='required_resources_list'),
    path('required_resources_update/<pk>/', RequiredResourcesUpdateView.as_view(), name='required_resources_update'),
    path('required_resources_delete/<pk>/', RequiredResourcesDeleteView.as_view(), name='required_resources_delete'),
    path('build_factory_create/', BuildFactoryCreateView.as_view(), name='build_factory_create'),
    path('build_factory_list/', BuildFactoryListView.as_view(), name='build_factory_list'),
    path('build_factory_update/<pk>/', BuildFactoryUpdateView.as_view(), name='build_factory_update'),
    path('build_factory_delete/<pk>/', BuildFactoryDeleteView.as_view(), name='build_factory_delete'),
    
    
]
