# Generated by Django 3.1.2 on 2020-12-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='user',
            field=models.TextField(),
        ),
    ]
