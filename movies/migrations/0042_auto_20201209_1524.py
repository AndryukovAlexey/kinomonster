# Generated by Django 3.1.2 on 2020-12-09 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0041_auto_20201208_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RemoveField(
            model_name='comments',
            name='serial',
        ),
    ]
