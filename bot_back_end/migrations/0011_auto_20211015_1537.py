# Generated by Django 3.2.8 on 2021-10-15 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_back_end', '0010_relationship_code_region_and_filial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Relationship_code_region_and_filial',
            new_name='Relate_code_region_and_filial',
        ),
        migrations.AlterModelOptions(
            name='relate_code_region_and_filial',
            options={'verbose_name': 'Регион филиала', 'verbose_name_plural': 'Регионы филиалов'},
        ),
    ]
