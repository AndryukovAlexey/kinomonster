# Generated by Django 3.1.2 on 2020-11-16 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201116_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='user',
            new_name='userka',
        ),
    ]
