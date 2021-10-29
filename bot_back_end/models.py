from django.db import models
from datetime import datetime
from django.contrib import admin
from django.shortcuts import get_object_or_404


# Create your models here.
class Three_categories(models.Model):
    """модель для представления таблицы
       текст - категория
    """
    text = models.CharField('ключ. слово', max_length=50)
    category = models.IntegerField('номер категории')
    def __str__(self):
        return self.text
    @admin.display(
        boolean=False,
        ordering='category',
        description='Категория',
    )
    def get_name_category(self):
        name_category_bool = Category_2_name_category.objects.filter(category=self.category)
        if name_category_bool:
            name_category = Category_2_name_category.objects.get(category=self.category)
            return name_category
        else:
            return f'Установите категорию:{self.category}'
    class Meta:
            verbose_name = 'Ключевое слово'
            verbose_name_plural = 'Ключевые слова'


class Category_managers(models.Model):
    """модель для представления информации
       о менеджере - ключю слово, имя,
       доб. номер
    """
    text = models.CharField('ключ. слово', max_length=50)
    name_man = models.CharField('имя менеджера', max_length=100)
    phone_number = models.CharField('доб. номер', max_length=12)
    def __str__(self):
        return self.text
    class Meta:
            verbose_name = 'Менеджер'
            verbose_name_plural = 'Менеджеры'


class Code_filial_2_name_filial(models.Model):
    """модель для представления
       цифрового кода филиала и названия филиала
    """
    code_filial = models.IntegerField('код города филиала')
    filial = models.CharField('название филиала', max_length=50)
    def __str__(self):
        return self.filial
    @admin.display(
        boolean=True,
        ordering='filial',
        description='время работы установлено?',
    )
    def was_set_worktime(self):
        worktime_bool = Worktime.objects.filter(filial=self.filial)
        if worktime_bool:
            return True
        else:
            return False
    class Meta:
            verbose_name = 'Филиал'
            verbose_name_plural = 'Филиалы'


class Depart_filial_2_phone_number(models.Model):
    """модель представления
       добавочного номера отдела в
       зависимости от филиала
    """
    depart = models.CharField('отдел', max_length=50)
    filial = models.CharField('филиал', max_length=50)
    phone_number = models.IntegerField('доб. номер')
    info = models.CharField('инфо', max_length=50)
    def __str__(self):
        return self.depart
    @admin.display(
        boolean=False,
        ordering='depart',
        description='доб.номер филиалов установлен?',
    )
    def was_set_filial(self):
        filials_from_depart_table = Depart_filial_2_phone_number.objects.filter(depart=self.depart).values_list('filial')
        filials_from_filial_table = Code_filial_2_name_filial.objects.all().values_list('filial')
        filial_bool = set(filials_from_filial_table) - set(filials_from_depart_table)
        if filial_bool:
            return filial_bool
        else:
            return 'OK'
    class Meta:
            verbose_name = 'Доб.номер отдела'
            verbose_name_plural = 'Доб.номера отделов'


class Worktime(models.Model):
    """модель для представления
       времени работы филиала
    """
    filial = models.CharField('филиал', max_length=50)
    time_open = models.TimeField('Начало рабочего дня')
    time_close =models.TimeField('Конец рабочего дня')
    def __str__(self):
        return self.filial
    class Meta:
            verbose_name = 'Время работы'
            verbose_name_plural = 'Время работы'


class Repeat_hallo(models.Model):
    """модель для представления
       фразы, когда человек говорит 'алло'
       или другое слово с временем задержки
       для ожидания следующего за 'алло' слова
    """
    time_repeat = models.FloatField('время в секундах после фразы клиента')
    times_repeat= models.IntegerField('количестово повторов')
    phrase_repeat=models.CharField('фраза для повтора', max_length=50)
    def __str__(self):
        return self.phrase_repeat
    class Meta:
            verbose_name = 'Фраза: я вас слушаю'
            verbose_name_plural = 'Фразы: я вас слушаю'


class Category_2_name_category(models.Model):
    """модель для представления
       цифрового номера категории
       и названия категории
    """
    category = models.IntegerField('номер категории')
    name_category = models.CharField('название категории', max_length=20)
    def __str__(self):
        return self.name_category
    @admin.display(
        boolean=True,
        ordering='category',
        description='доб.номер отдела установлен?',
    )
    def was_set_added_phone_number(self):
        set_added_phone_number_bool = Depart_filial_2_phone_number.objects.filter(depart=self.name_category)
        if set_added_phone_number_bool:
            return True
        else:
            return False
    class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'


class Regions_name_and_code(models.Model):
    """модель для представления
       кода региона
       и названия региона
    """
    code_region = models.IntegerField('код региона')
    name_region = models.CharField('название региона', max_length=100)
    def __str__(self):
        return self.name_region
    @admin.display(
        boolean=True,
        ordering='code_region',
        description='филиал установлен?',
    )
    def is_set_filial(self):
        available_filial_bool = Relate_code_region_and_filial.objects.filter(code_region=self.code_region)
        if available_filial_bool:
            return True
        else:
            return False
    class Meta:
            verbose_name = 'Регион'
            verbose_name_plural = 'Регионы'


class Relate_code_region_and_filial(models.Model):
    """модель для представления
       кода региона
       и кода филиала
    """
    code_region = models.IntegerField('код региона')
    code_filial = models.IntegerField('код филиала')
    def __str__(self):
        return Regions_name_and_code.objects.get(code_region=self.code_region).name_region
    @admin.display(
        boolean=False,
        ordering='code_filial',
        description='филиал',
    )
    def get_filial(self):
        filial = Code_filial_2_name_filial.objects.get(code_filial=self.code_filial).filial
        return filial
    @admin.display(
        boolean=False,
        ordering='code_filial',
        description='регион',
    )
    def get_region(self):
        name_region = Regions_name_and_code.objects.get(code_region=self.code_region).name_region
        return name_region

    class Meta:
            verbose_name = 'Регион филиала'
            verbose_name_plural = 'Регионы филиалов'


class Calltrack_lite(models.Model):
    id_rec = models.CharField('ID из астериск', max_length=14)
    text = models.TextField('фраза клиента', default='')
    text_lemm = models.TextField('нормализированная фраза', default='')
    date_time_calling = models.DateTimeField('время звонка', default=datetime.now())
    innumber = models.CharField('номер тел.', max_length=11)
    region = models.IntegerField('код региона')
    dial_route = models.IntegerField('доб. номер')
    key_words = models.CharField('кл. слова', max_length=150)
    @admin.display(
        boolean=False,
        ordering='region',
        description='регион',
    )
    def get_region(self):
        name_region = Regions_name_and_code.objects.get(code_region=self.region).name_region
        return name_region
    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'