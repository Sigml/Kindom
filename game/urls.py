from django.urls import path
from .views import NewWorldCreateView, SelectGameView, InGameView, DeleteGameDeleteView, update_game_day, unlock_technology

urlpatterns = [
    path('create_new_world/', NewWorldCreateView.as_view(), name='create_new_world'),
    path('select_game/', SelectGameView.as_view(), name='select_game'),
    path('delete_game/<pk>', DeleteGameDeleteView.as_view(), name='delete_game'),
    path('in_game/<int:pk>/', InGameView.as_view(), name='in_game'),
    path('update_game_day/<int:pk>/', update_game_day, name='update_game_day'),
    path('unlock_technology/<int:pk>/<int:technology_pk>/', unlock_technology, name='unlock_technology'),
    
]