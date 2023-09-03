from django.contrib import admin

from dogs.models import Dogs, Breed


@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed')
    list_filter = 'breed',


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
