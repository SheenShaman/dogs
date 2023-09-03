from django.shortcuts import render
from dogs.models import Breed, Dogs


def index(request):
    context = {
        'object_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds(request):
    context = {
        'object_list': Breed.objects.all(),
        'title': 'Питомник - все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


def breed_dogs(request, pk):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        'object_list': Dogs.objects.filter(breed_id=pk),
        'title': f'Собаки породы - все наши породы {breed_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)
