# Generated by Django 3.2.8 on 2021-11-02 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0006_alter_calltrack_lite_date_time_calling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltrack_lite',
            name='date_time_calling',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 15, 44, 3, 651990), verbose_name='время звонка'),
        ),
    ]