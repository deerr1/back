# Generated by Django 3.0 on 2020-12-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoInstitutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.IntegerField(choices=[(0, 'oil'), (1, 'hum'), (2, 'leg'), (3, 'dig')], verbose_name='Псвевдоним института')),
                ('direction', models.CharField(max_length=30, verbose_name='Направление подготовки')),
                ('specialty', models.CharField(max_length=30, verbose_name='Cпециальность')),
                ('qualification', models.CharField(max_length=30, verbose_name='Квалификация')),
                ('preparation', models.CharField(max_length=40, verbose_name='Профиль подготовки')),
                ('form', models.IntegerField(choices=[(0, 'очная'), (1, 'заочная')], verbose_name='Форма обучения')),
                ('training_period', models.IntegerField(verbose_name='Срок обучения')),
                ('number_of_budget', models.IntegerField(verbose_name='Количество бюджетных мест')),
                ('number_of_paid', models.IntegerField(verbose_name='Количество платных мест')),
                ('passing_score', models.IntegerField(verbose_name='Проходной балл на бюджет по итогам предыдущего года')),
                ('info', models.TextField(verbose_name='Информация о направлении')),
                ('professions', models.TextField(verbose_name='Професии')),
                ('points', models.ManyToManyField(to='Institutions.Points', verbose_name='Минимальный балл для участия в конкурсе')),
            ],
            options={
                'verbose_name_plural': 'Направления',
            },
        ),
    ]