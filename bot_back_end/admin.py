from django.contrib import admin

# Register your models here.
from .models import Three_categories, Category_managers, Category_2_depart
from .models import Code_filial_2_name_filial, Depart_filial_2_phone_number
from .models import Worktime

admin.site.register(Three_categories)
admin.site.register(Category_managers)
admin.site.register(Category_2_depart)
admin.site.register(Code_filial_2_name_filial)
admin.site.register(Depart_filial_2_phone_number)
admin.site.register(Worktime)