# Generated by Django 4.2.4 on 2023-09-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кличка')),
                ('description', models.CharField(max_length=50, verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кличка')),
                ('breed', models.CharField(max_length=50, verbose_name='Порода')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='Фотография')),
                ('b_day', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
    ]
