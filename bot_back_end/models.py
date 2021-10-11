from django.db import models

# Create your models here.
class Three_categories(models.Model):
    text = models.CharField('key word', max_length=50)
    category = models.CharField('category of word (or depart)', max_length=50)
    def __str__(self):
        return self.text


class Category_managers(models.Model):
    text = models.CharField('key word', max_length=50)
    name_man = models.CharField('name of manager', max_length=100)
    phone_number = models.CharField(max_length=12)
    def __str__(self):
        return self.text


class Code_filial_2_name_filial(models.Model):
    code_filial = models.IntegerField('city code of filial')
    name = models.CharField('name of city filial', max_length=100)
    def __str__(self):
        return self.name


class Depart_filial_2_phone_number(models.Model):
    depart = models.CharField('name of depart (or category)', max_length=50)
    filial = models.CharField('name of city filial', max_length=50)
    phone_number = models.IntegerField('phone number')
    info = models.CharField('info about depart', max_length=50)
    def __str__(self):
        return self.depart


class Worktime(models.Model):
    filial = models.CharField('name of city filial', max_length=50)
    time_open = models.TimeField('time open')
    time_close =models.TimeField('time close')
    def __str__(self):
        return self.filial