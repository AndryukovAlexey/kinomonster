# Generated by Django 3.1.2 on 2020-11-16 16:36

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.IntegerField(verbose_name=django.contrib.auth.models.User),
        ),
    ]