from django.contrib import admin

# Register your models here.
from .models import Three_categories, Category_managers
from .models import Code_filial_2_name_filial, Depart_filial_2_phone_number
from .models import Worktime, Repeat_hallo, Category_2_name_category
from .models import Regions_name_and_code, Relate_code_region_and_filial
from .models import Calltrack_lite, Departs
from .views import export_calltrack_xls

class FilialAdmin(admin.ModelAdmin):
    fields=['filial','code_filial']
    list_display = ('filial', 'code_filial', 'was_set_worktime')
    list_filter = ['filial']


class Three_categoriesAdmin(admin.ModelAdmin):
    fields=['text','category']
    list_display = ('text', 'get_name_category')
    ordering = ['text']
    list_filter = ['category']
    search_fields = ['text']


class Category_managersAdmin(admin.ModelAdmin):
    fields=['text', 'phone_number', 'name_man']
    list_display = ('name_man', 'phone_number', 'text')
    ordering = ['name_man', 'text']
    search_fields = ['text']


class Depart_filial_2_phone_numberAdmin(admin.ModelAdmin):
    fields=['depart', 'filial', 'phone_number', 'info']
    list_display = ('depart', 'filial', 'phone_number', 'info', 'was_set_filial')


class WorktimeAdmin(admin.ModelAdmin):
    fields=['filial', 'time_open', 'time_close']
    list_display = ('filial', 'time_open', 'time_close')
    ordering = ['time_open']


class Repeat_halloAdmin(admin.ModelAdmin):
    fields=['phrase_repeat', 'time_repeat', 'times_repeat']
    list_display = ('phrase_repeat', 'time_repeat', 'times_repeat')


class Category_2_name_categoryAdmin(admin.ModelAdmin):
    fields=['name_category', 'category']
    list_display = ('name_category', 'category', 'was_set_added_phone_number')
    ordering = ['name_category', 'category']


class Regions_name_and_codeAdmin(admin.ModelAdmin):
    fields=['name_region', 'code_region']
    list_display = ('name_region', 'code_region', 'was_set_filial')
    list_filter = ['name_region']
    ordering = ['name_region']


class Relate_code_region_and_filialAdmin(admin.ModelAdmin):
    fields=['code_region', 'code_filial']
    list_display = ('get_region', 'get_filial')
    list_filter = ['code_filial']
    ordering = ['code_region', 'code_filial']


class Calltrack_liteAdmin(admin.ModelAdmin):
    fields=['id_rec', 'text', 'text_lemm', 'date_time_calling',
            'innumber', 'region', 'dial_route', 'key_words']
    list_display = ['date_time_calling', 'innumber', 'text',
                    'key_words', 'get_depart', 'get_region']
    ordering = ['date_time_calling', 'id_rec']
    list_filter = ['date_time_calling']
    actions = ['get_calltrack_xls']

    @admin.action(description='Выгрузить таблицу звонков')
    def get_calltrack_xls(modeladmin, request, queryset):
        return export_calltrack_xls(request)

class DepartsAdmmin(admin.ModelAdmin):
    fields = ['depart_name', 'depart_added_phone_number']
    list_display = ['depart_name', 'depart_added_phone_number']
    ordering = ['depart_added_phone_number']


admin.site.register(Code_filial_2_name_filial, FilialAdmin)
admin.site.register(Three_categories, Three_categoriesAdmin)
admin.site.register(Category_managers, Category_managersAdmin)
admin.site.register(Depart_filial_2_phone_number, Depart_filial_2_phone_numberAdmin)
admin.site.register(Worktime, WorktimeAdmin)
admin.site.register(Repeat_hallo, Repeat_halloAdmin)
admin.site.register(Category_2_name_category, Category_2_name_categoryAdmin)
admin.site.register(Regions_name_and_code, Regions_name_and_codeAdmin)
admin.site.register(Relate_code_region_and_filial, Relate_code_region_and_filialAdmin)
admin.site.register(Calltrack_lite, Calltrack_liteAdmin)
admin.site.register(Departs, DepartsAdmmin)