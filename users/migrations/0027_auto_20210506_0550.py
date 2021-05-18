# Generated by Django 3.1.2 on 2021-05-06 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20210424_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premka',
            name='date_end',
            field=models.DateField(default=datetime.date(2021, 6, 6), verbose_name='дата окончани'),
        ),
        migrations.AlterField(
            model_name='premka',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 5, 6), verbose_name='дата покупки'),
        ),
    ]
