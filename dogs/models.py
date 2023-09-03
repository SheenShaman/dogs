from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Dogs(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кличка')
    breed = models.ForeignKey('Breed', verbose_name='Порода', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Фотография')
    b_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name}({self.breed})'

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'


class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='Порода')
    description = models.CharField(max_length=50, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
