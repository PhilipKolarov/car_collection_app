# Generated by Django 4.1.2 on 2022-10-30 07:55

import car_collection_app.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[car_collection_app.web.models.username_length_validator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
