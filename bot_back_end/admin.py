from django.contrib import admin

# Register your models here.
from .models import Three_categories, Category_managers
from .models import Code_filial_2_name_filial, Depart_filial_2_phone_number
from .models import Worktime


class Depart_filial_2_phone_numberInlines(admin.StackedInline):
    model = Depart_filial_2_phone_number
    extra = 3


class FilialInfo(admin.ModelAdmin):
    fieldsets =[
        ('Названиe филиала',                  {'fields': ['name']}),
        ('Код филиала',         {'fields': ['code_filial']}),
    ]
    #inlines = [Depart_filial_2_phone_numberInlines]


admin.site.register(Code_filial_2_name_filial, FilialInfo)
admin.site.register(Three_categories)
admin.site.register(Category_managers)
admin.site.register(Depart_filial_2_phone_number)
admin.site.register(Worktime)