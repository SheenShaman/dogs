from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from dogs.models import Breed, Dogs


class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Питомник - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data

# def index(request):
#     context = {
#         'object_list': Breed.objects.all()[:3],
#         'title': 'Питомник - Главная'
#     }
#     return render(request, 'dogs/index.html', context)


# def breeds(request):
#     context = {
#         'object_list': Breed.objects.all(),
#         'title': 'Питомник - все наши породы'
#     }
#     return render(request, 'dogs/breed_list.html', context)


class BreedListView(ListView):
    model = Breed
    extra_context = {
        'title': 'Питомник - все наши породы'
    }


# def breed_dogs(request, pk):
#     breed_item = Breed.objects.get(pk=pk)
#     context = {
#         'object_list': Dogs.objects.filter(breed_id=pk),
#         'title': f'Собаки породы - все наши породы {breed_item.name}'
#     }
#     return render(request, 'dogs/dogs_list.html', context)

class DogListView(ListView):
    model = Dogs

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['breed_pk'] = breed_item.pk,
        context_data['title'] = f'Собаки породы - все наши породы {breed_item.name}'
        return context_data


class DogCreateView(CreateView):
    model = Dogs
    fields = ('name', 'breed', )
    success_url = reverse_lazy('dogs:breeds')


class DogUpdateView(UpdateView):
    model = Dogs
    fields = ('name', 'breed', )

    def get_success_url(self):
        return reverse('dogs:breed', args=[self.object.breed.pk])


class DogDeleteView(DeleteView):
    model = Dogs
    success_url = reverse_lazy('dogs:breeds')

