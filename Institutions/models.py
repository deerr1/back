from django.db import models

# Create your models here.


class Subjects(models.Model):
    """
    Предметы ЕГЭ для направления
    """

    subject = models.CharField(max_length=30, blank=False, verbose_name='Предмет')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name_plural = 'Предметы'

class Points(models.Model):
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,verbose_name='Предмет')
    point = models.IntegerField(verbose_name='Количество баллов')
    mandatory =models.BooleanField(default=True,verbose_name='Обязательность сдачи')

    def __str__(self):
        return f'{self.subject} {self.point}'

    class Meta:
        verbose_name_plural = 'Минимальные баллы'

# class SubjectsPoints(models.Model):

    

class InfoInstitutions(models.Model):
    INST_ALIAS=(
        (0,'oil'),
        (1,'hum'),
        (2,'leg'),
        (3,'dig')
    )
    FORM=(
        (0,'очная'),
        (1,'заочная')
    )

    alias = models.IntegerField(choices = INST_ALIAS, verbose_name='Псвевдоним института')
    direction = models.CharField(max_length=30, blank=False, verbose_name='Направление подготовки')
    specialty = models.CharField(max_length=30, blank=False, verbose_name='Cпециальность')
    qualification = models.CharField(max_length=30, blank=False, verbose_name='Квалификация')
    preparation = models.CharField(max_length=40, blank=False, verbose_name='Профиль подготовки')
    form = models.IntegerField(choices = FORM, verbose_name='Форма обучения')
    training_period = models.IntegerField(verbose_name='Срок обучения')
    number_of_budget = models.IntegerField(verbose_name='Количество бюджетных мест')
    number_of_paid = models.IntegerField(verbose_name='Количество платных мест')
    points = models.ManyToManyField(Points, verbose_name='Минимальный балл для участия в конкурсе')
    passing_score = models.IntegerField(verbose_name='Проходной балл на бюджет по итогам предыдущего года')
    info = models.TextField(verbose_name='Информация о направлении')
    professions = models.TextField(verbose_name='Професии')
    foto = models.ImageField(upload_to='images_inst/',verbose_name='Фотография для страницы направления', default='img.jpg')

    def __str__(self):
        return f'{self.alias} {self.direction} {self.specialty}'

    class Meta:
        verbose_name_plural = 'Направления'