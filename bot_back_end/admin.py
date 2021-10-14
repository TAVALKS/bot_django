from django.contrib import admin

# Register your models here.
from .models import Three_categories, Category_managers
from .models import Code_filial_2_name_filial, Depart_filial_2_phone_number
from .models import Worktime, Repeat_hallo, Category_2_name_category


class FilialAdmin(admin.ModelAdmin):
    fields=['filial','code_filial']
    list_display = ('filial', 'code_filial', 'was_set_worktime')
    list_filter = ['filial']


class Three_categoriesAdmin(admin.ModelAdmin):
    fields=['text','category']
    list_display = ('text','category', 'get_name_category')


class Category_managersAdmin(admin.ModelAdmin):
    fields=['text', 'phone_number', 'name_man']
    list_display = ('text', 'phone_number', 'name_man')


class Depart_filial_2_phone_numberAdmin(admin.ModelAdmin):
    fields=['depart', 'filial', 'phone_number', 'info']
    list_display = ('depart', 'filial', 'phone_number', 'info', 'was_set_filial')


class WorktimeAdmin(admin.ModelAdmin):
    fields=['filial', 'time_open', 'time_close']
    list_display = ('filial', 'time_open', 'time_close')


class Repeat_halloAdmin(admin.ModelAdmin):
    fields=['phrase_repeat', 'time_repeat', 'times_repeat']
    list_display = ('phrase_repeat', 'time_repeat', 'times_repeat')


class Category_2_name_categoryAdmin(admin.ModelAdmin):
    fields=['name_category', 'category']
    list_display = ('name_category', 'category')


admin.site.register(Code_filial_2_name_filial, FilialAdmin)
admin.site.register(Three_categories, Three_categoriesAdmin)
admin.site.register(Category_managers, Category_managersAdmin)
admin.site.register(Depart_filial_2_phone_number, Depart_filial_2_phone_numberAdmin)
admin.site.register(Worktime, WorktimeAdmin)
admin.site.register(Repeat_hallo, Repeat_halloAdmin)
admin.site.register(Category_2_name_category, Category_2_name_categoryAdmin)