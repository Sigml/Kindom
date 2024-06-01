from django.urls import path, include
from .views import (AgeCreateView, AgeListView, AgeUpdateView, AgeDeleteView, CountryCreateView, CountryListView, 
                    CountryUpdateView, CountryDeleteView, ResourcesCreateView, ResourcesListView, ResourcesUpdateView,
                    ResourcesDeleteView, FactoryCreateView, FactoryListView, FactoryUpdateView, FactoryDeleteView,
                    RequiredResourcesCreateView, RequiredResourcesListView, RequiredResourcesUpdateView, RequiredResourcesDeleteView,
                    BuildFactoryCreateView, BuildFactoryListView, BuildFactoryUpdateView, BuildFactoryDeleteView, EcologyCreateView,
                    EcologyListView, EcologyUpdateView, EcologyDeleteView, TradeCreateView, TradeListView, TradeUpdateView, TradeDeleteView,
                    AllianceCreateView, AllianceListView, AllianceUpdateView, AllianceDeleteView, TradeAgreementCreateView,
                    TradeAgreementListView, TradeAgreementUpdateView, TradeAgreementDeleteView, PeaceTreatyCreateView, PeaceTreatyListView,
                    PeaceTreatyDeleteView, PeaceTreatyUpdateView, ArmyCreateView, ArmyListView, ArmyUpdateView,
                    ArmyDeleteView, WarCreateView, WarListView, WarUpdateView, WarDeleteView, TechnologyCreateView, TechnologyListView,
                    TechnologyDeleteView, TechnologyUpdateView, EventCreateView, EventListView, EventUpdateView, EventDeleteView,     
                    SocialDevelopmentCreateView, SocialDevelopmentListView, SocialDevelopmentUpdateView, SocialDevelopmentDeleteView, 
                    
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
    path('ecology_create/', EcologyCreateView.as_view(), name='ecology_create'),
    path('ecology_list/', EcologyListView.as_view(), name='ecology_list'),
    path('ecology_update/<pk>/', EcologyUpdateView.as_view(), name='ecology_update'),
    path('ecology_delete/<pk>/', EcologyDeleteView.as_view(), name='ecology_delete'),
    path('trade_create/', TradeCreateView.as_view(), name='trade_create'),
    path('trade_list/', TradeListView.as_view(), name='trade_list'),
    path('trade_update/<pk>/', TradeUpdateView.as_view(), name='trade_update'),
    path('trade_delete/<pk>/', TradeDeleteView.as_view(), name='trade_delete'),
    path('alliance_create/', AllianceCreateView.as_view(), name='alliance_create'),
    path('alliance_list/', AllianceListView.as_view(), name='alliance_list'),
    path('alliance_update/<pk>/', AllianceUpdateView.as_view(), name='alliance_update'),
    path('alliance_delete/<pk>/', AllianceDeleteView.as_view(), name='alliance_delete'),
    path('trade_agreement_create/', TradeAgreementCreateView.as_view(), name='trade_agreement_create'),
    path('trade_agreement_list/', TradeAgreementListView.as_view(), name='trade_agreement_list'),
    path('trade_agreement_update/<pk>/', TradeAgreementUpdateView.as_view(), name='trade_agreement_update'),
    path('trade_agreement_delete/<pk>/', TradeAgreementDeleteView.as_view(), name='trade_agreement_delete'),
    path('peace_treaty_create/', PeaceTreatyCreateView.as_view(), name='peace_treaty_create'),
    path('peace_treaty_list/', PeaceTreatyListView.as_view(), name='peace_treaty_list'),
    path('peace_treaty_update/<pk>/', PeaceTreatyUpdateView.as_view(), name='peace_treaty_update'),
    path('peace_treaty_delete/<pk>/', PeaceTreatyDeleteView.as_view(), name='peace_treaty_delete'),
    path('army_create/', ArmyCreateView.as_view(), name='army_create'),
    path('army_list/', ArmyListView.as_view(), name='army_list'),
    path('army_update/<pk>/', ArmyUpdateView.as_view(), name='army_update'),
    path('army_delete/<pk>/', ArmyDeleteView.as_view(), name='army_delete'),
    path('war_create/', WarCreateView.as_view(), name='war_create'),
    path('war_list/', WarListView.as_view(), name='war_list'),
    path('war_update/<pk>/', WarUpdateView.as_view(), name='war_update'),
    path('war_delete/<pk>/', WarDeleteView.as_view(), name='war_delete'),
    path('technology_create/', TechnologyCreateView.as_view(), name='technology_create'),
    path('technology_list/', TechnologyListView.as_view(), name='technology_list'),
    path('technology_update/<pk>/', TechnologyUpdateView.as_view(), name='technology_update'),
    path('technology_delete/<pk>/', TechnologyDeleteView.as_view(), name='technology_delete'),
    path('event_create/', EventCreateView.as_view(), name='event_create'),
    path('event_list/', EventListView.as_view(), name='event_list'),
    path('event_update/<pk>/', EventUpdateView.as_view(), name='event_update'),
    path('event_delete/<pk>/', EventDeleteView.as_view(), name='event_delete'),
    path('social_development_create/', SocialDevelopmentCreateView.as_view(), name='social_development_create'),
    path('social_development_list/', SocialDevelopmentListView.as_view(), name='social_development_list'),
    path('social_development_update/<pk>/', SocialDevelopmentUpdateView.as_view(), name='social_development_update'),
    path('social_development_delete/<pk>/', SocialDevelopmentDeleteView.as_view(), name='social_development_delete'),

]
