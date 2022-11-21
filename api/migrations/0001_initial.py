# Generated by Django 4.1.3 on 2022-11-21 17:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('lastName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True, unique=True)),
                ('dateOfBirth', models.DateField(null=True)),
                ('bankAccount', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('farmer', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('units', models.CharField(choices=[('Kg', 'Kg'), ('Kus', 'Kus')], default='Kg', max_length=3)),
                ('price', models.IntegerField()),
                ('placeOfOrigin', models.CharField(max_length=100)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cropsByFarmer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CropCatalog',
            fields=[
                ('cropType', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Zelenina', 'Zelenina'), ('Ovoce', 'Ovoce')], default='Zelenina', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('timeFrom', models.TimeField()),
                ('timeTo', models.TimeField()),
                ('price', models.IntegerField()),
                ('units', models.CharField(choices=[('Kg', 'Kg'), ('Kus', 'Kus')], default='Kg', max_length=3)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cropcatalog')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('postAddress', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropType', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(choices=[('Zelenina', 'Zelenina'), ('Ovoce', 'Ovoce')], default='Zelenina', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.crop')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cropsByType', to='api.cropcatalog'),
        ),
        migrations.CreateModel(
            name='HarvestUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.harvest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('harvest', 'user')},
            },
        ),
    ]
