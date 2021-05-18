# Generated by Django 3.1.2 on 2020-12-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0032_comments_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='serial',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.serials'),
        ),
    ]
