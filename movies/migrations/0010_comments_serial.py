# Generated by Django 3.1.2 on 2020-12-07 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20201207_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='serial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.serials'),
        ),
    ]
