# Generated by Django 3.1.2 on 2020-12-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0025_remove_comments_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
    ]