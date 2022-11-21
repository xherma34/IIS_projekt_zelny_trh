# Generated by Django 4.1.3 on 2022-11-21 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='crop',
            name='placeOfOrigin',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='crop',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cropcatalog',
            name='category',
            field=models.CharField(choices=[('Zelenina', 'Zelenina'), ('Ovoce', 'Ovoce')], default='Zelenina', max_length=50),
        ),
        migrations.AlterField(
            model_name='cropcatalog',
            name='cropType',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='city',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='order',
            name='postAddress',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='category',
            field=models.CharField(choices=[('Zelenina', 'Zelenina'), ('Ovoce', 'Ovoce')], default='Zelenina', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='bankAccount',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]