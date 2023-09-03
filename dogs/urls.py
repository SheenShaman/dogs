from django.urls import path
from dogs.views import index, breeds, breed_dogs
from dogs.apps import DogsConfig


app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('breeds/', breeds, name='breeds'),
    path('<int:pk>/dogs/', breed_dogs, name='breed_dogs'),
]
