from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from dogs.forms import DogForm, ParentForm
from dogs.models import Breed, Dogs, Parent


class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Питомник - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


class BreedListView(ListView):
    model = Breed
    extra_context = {
        'title': 'Питомник - все наши породы'
    }


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
    form_class = DogForm
    success_url = reverse_lazy('dogs:breeds')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        
        return super().form_valid(form)

class DogUpdateView(UpdateView):
    model = Dogs
    form_class = DogForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Dogs, Parent, form=ParentForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dogs:dog_update', args=[self.kwargs.get('pk')])


class DogDeleteView(DeleteView):
    model = Dogs
    success_url = reverse_lazy('dogs:breeds')

