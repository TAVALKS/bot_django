# Generated by Django 3.2.8 on 2021-11-09 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0009_alter_calltrack_lite_date_time_calling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltrack_lite',
            name='date_time_calling',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 10, 7, 20, 141389), verbose_name='время звонка'),
        ),
        migrations.AlterField(
            model_name='calltrack_lite',
            name='id_rec',
            field=models.CharField(max_length=15, verbose_name='ID из астериск'),
        ),
    ]
