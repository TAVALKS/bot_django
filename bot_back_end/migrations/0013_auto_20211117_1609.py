# Generated by Django 3.2.8 on 2021-11-17 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0012_alter_calltrack_lite_date_time_calling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltrack_lite',
            name='date_time_calling',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 16, 9, 20, 328963), verbose_name='время звонка'),
        ),
        migrations.AlterField(
            model_name='calltrack_lite',
            name='id_rec',
            field=models.CharField(max_length=20, verbose_name='ID из астериск'),
        ),
    ]