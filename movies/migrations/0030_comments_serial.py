# Generated by Django 3.1.2 on 2020-12-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0029_remove_comments_ser'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='serial',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='movies.serials'),
        ),
    ]