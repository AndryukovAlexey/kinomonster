# Generated by Django 3.1.2 on 2020-12-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0050_auto_20201218_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='name',
            field=models.CharField(default='', max_length=70, verbose_name='Название'),
        ),
    ]