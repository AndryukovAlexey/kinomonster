# Generated by Django 3.1.2 on 2020-12-07 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
    ]