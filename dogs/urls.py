from django.urls import path
from dogs.views import IndexView, BreedListView, DogListView, DogCreateView, DogUpdateView, DogDeleteView
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('breeds/', BreedListView.as_view(), name='breeds'),
    path('dogs/<int:pk>/', DogListView.as_view(), name='breed'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]
