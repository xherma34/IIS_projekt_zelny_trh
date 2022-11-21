# Generated by Django 4.1.3 on 2022-11-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_crop_image_cropcatalog_image_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Zelenina', 'Zelenina'), ('Ovoce', 'Ovoce')], default='Zelenina', max_length=100)),
            ],
        ),
    ]
