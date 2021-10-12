from django.db import models
from django.contrib import admin
from django.shortcuts import get_object_or_404

# Create your models here.
class Three_categories(models.Model):
    text = models.CharField('ключ. слово', max_length=50)
    category = models.CharField('категория ключ. слово (отдел или категория)', max_length=50)
    def __str__(self):
        return self.text
    class Meta:
            verbose_name = 'Ключевое слово'
            verbose_name_plural = 'Ключевые слова'


class Category_managers(models.Model):
    text = models.CharField('ключ. слово', max_length=50)
    name_man = models.CharField('имя менеджера', max_length=100)
    phone_number = models.CharField('доб. номер', max_length=12)
    def __str__(self):
        return self.text
    class Meta:
            verbose_name = 'Менеджер'
            verbose_name_plural = 'Менеджеры'


class Code_filial_2_name_filial(models.Model):
    code_filial = models.IntegerField('код города филиала')
    name = models.CharField('название филиала', max_length=50)
    def __str__(self):
        return self.name
    @admin.display(
        boolean=True,
        ordering='name',
        description='время работы установлено?',
    )
    def was_set_worktime(self):
        worktime_bool = Worktime.objects.filter(filial=self.name)
        if worktime_bool:
            return True
        else:
            return False
    class Meta:
            verbose_name = 'Название филиала'
            verbose_name_plural = 'Назавания филиалов'


class Depart_filial_2_phone_number(models.Model):
    depart = models.CharField('отдел', max_length=50)
    filial = models.CharField('город филиала', max_length=50)
    phone_number = models.IntegerField('доб. номер')
    info = models.CharField('инфо', max_length=50)
    def __str__(self):
        return self.depart
    class Meta:
            verbose_name = 'Доб.номер отдела'
            verbose_name_plural = 'Доб.номера отделов'


class Worktime(models.Model):
    filial = models.CharField('филиал', max_length=50)
    time_open = models.TimeField('Начало рабочего дня')
    time_close =models.TimeField('Конец рабочего дня')
    def __str__(self):
        return self.filial
    class Meta:
            verbose_name = 'Время работы'
            verbose_name_plural = 'Время работы'


class Repeat_hallo(models.Model):
    time_repeat = models.FloatField('время в секундах после фразы клиента')
    times_repeat= models.IntegerField('количестово повторов')
    phrase_repeat=models.CharField('фраза для повтора', max_length=50)
    def __str__(self):
        return self.phrase_repeat
    class Meta:
            verbose_name = 'Фраза: я вас слушаю'
            verbose_name_plural = 'Фразы: я вас слушаю'