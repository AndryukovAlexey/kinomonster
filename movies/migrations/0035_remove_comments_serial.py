# Generated by Django 3.1.2 on 2020-12-08 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0034_auto_20201208_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='serial',
        ),
    ]