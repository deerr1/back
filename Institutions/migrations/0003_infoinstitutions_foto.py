# Generated by Django 3.0 on 2020-12-09 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institutions', '0002_infoinstitutions'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoinstitutions',
            name='foto',
            field=models.ImageField(default='img.jpg', upload_to='images_inst/', verbose_name='Фотография для страницы направления'),
        ),
    ]
