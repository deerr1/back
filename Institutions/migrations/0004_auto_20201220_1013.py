# Generated by Django 3.0 on 2020-12-20 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institutions', '0003_infoinstitutions_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoinstitutions',
            name='availability_of_budger',
            field=models.BooleanField(default=False, verbose_name='Наличие бюджетных мест'),
        ),
        migrations.AddField(
            model_name='infoinstitutions',
            name='availability_of_paid',
            field=models.BooleanField(default=False, verbose_name='Наличие платных мест'),
        ),
    ]
