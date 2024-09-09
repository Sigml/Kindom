from django.urls import path
from .views import NewWorldCreateView, InGameView

urlpatterns = [
    path('create_new_world/', NewWorldCreateView.as_view(), name='create_new_world'),
    path('in_game/', InGameView.as_view(), name='game')
]