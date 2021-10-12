from django.test import TestCase

from .models import Three_categories, Category_managers, Code_filial_2_name_filial #Import the model classes we just wrote.
from .models import Depart_filial_2_phone_number, Worktime #Import the model classes we just wrote.
# Create your tests here.

Worktime_test = Worktime(filial='Chelyabinsk')
print(Worktime_test)