from django.contrib import admin

# Register your models here.
from .models import Three_categories, Category_managers
from .models import Code_filial_2_name_filial, Depart_filial_2_phone_number
from .models import Worktime


class FilialAdmin(admin.ModelAdmin):
    fields=['name','code_filial']
    list_display = ('name', 'code_filial', 'was_set_worktime')
    list_filter = ['name']


class Three_categoriesAdmin(admin.ModelAdmin):
    fields=['text','category']
    list_display = ('text','category')


class Category_managersAdmin(admin.ModelAdmin):
    fields=['text', 'phone_number', 'name_man']
    list_display = ('text', 'phone_number', 'name_man')


class Depart_filial_2_phone_numberAdmin(admin.ModelAdmin):
    fields=['depart', 'filial', 'phone_number', 'info']
    list_display = ('depart', 'filial', 'phone_number', 'info')


class WorktimeAdmin(admin.ModelAdmin):
    fields=['filial', 'time_open', 'time_close']
    list_display = ('filial', 'time_open', 'time_close')


class Repeat_halloAdmin(admin.ModelAdmin):
    fields=['time_repeat', 'times_repeat', 'phrase_repeat']
    list_display = ('times_repeat', 'times_repeat', 'phrase_repeat')


admin.site.register(Code_filial_2_name_filial, FilialAdmin)
admin.site.register(Three_categories, Three_categoriesAdmin)
admin.site.register(Category_managers, Category_managersAdmin)
admin.site.register(Depart_filial_2_phone_number, Depart_filial_2_phone_numberAdmin)
admin.site.register(Worktime, WorktimeAdmin)
admin.site.register(Repeat_halloAdmin, Repeat_halloAdmin)