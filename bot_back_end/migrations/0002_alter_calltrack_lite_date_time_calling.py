# Generated by Django 3.2.8 on 2021-11-02 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltrack_lite',
            name='date_time_calling',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 15, 38, 29, 84636), verbose_name='время звонка'),
        ),
    ]
