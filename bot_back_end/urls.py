from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('export/xls/', views.export_calltrack_xls, name='export_calltrack_xls'),
]