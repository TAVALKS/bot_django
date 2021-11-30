from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('export/xls/', views.export_calltrack_xls, name='export_calltrack_xls'),
    path('get_depart_or_name_manager/', views.get_depart_or_name_manager, name='get_name_manager_or_depart'),
]