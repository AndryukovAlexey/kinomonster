# Generated by Django 3.1.2 on 2020-11-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201112_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='poster',
            field=models.ImageField(default='', upload_to='films/', verbose_name='изображение'),
        ),
    ]
