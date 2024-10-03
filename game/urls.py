from django.urls import path
from .views import NewWorldCreateView, SelectGameView, InGameView, DeleteGameDeleteView

urlpatterns = [
    path('create_new_world/', NewWorldCreateView.as_view(), name='create_new_world'),
    path('select_game/', SelectGameView.as_view(), name='select_game'),
    path('delete_game/<pk>', DeleteGameDeleteView.as_view(), name='delete_game'),
    path('in_game/<pk>/', InGameView.as_view(), name='in_game'),
]