# Generated by Django 3.2.8 on 2021-11-01 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0012_auto_20211022_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=150)),
                ('depart_added_phone_number', models.CharField(max_length=11, verbose_name='номер тел.')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.AlterModelOptions(
            name='calltrack_lite',
            options={'verbose_name': 'Звонок', 'verbose_name_plural': 'Звонки'},
        ),
        migrations.AlterField(
            model_name='calltrack_lite',
            name='date_time_calling',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 16, 46, 3, 38427), verbose_name='время звонка'),
        ),
    ]
