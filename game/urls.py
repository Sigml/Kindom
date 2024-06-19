from django.urls import path
from .views import New_World_Create_View

urlpatterns = [
    path('create_new_world/', New_World_Create_View.as_view(), name='create_new_world')
]