# Generated by Django 3.1.2 on 2020-12-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0048_auto_20201218_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.CharField(default='', max_length=70, null=True, verbose_name='user'),
        ),
    ]
