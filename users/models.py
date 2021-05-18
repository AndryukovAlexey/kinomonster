from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from dateutil.relativedelta import relativedelta
from pytils import translit


class Profile(models.Model):

    def get_image_path(self, filename):
        path = ''.join(["kinomonster/media/avatars/",translit.slugify(filename)])
        return path

    name = models.OneToOneField(User, verbose_name='Логин', on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.jpg', upload_to=get_image_path)

    def __str__(self):
        return f'{self.name.username}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Premka(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_start = models.DateField("дата покупки", default=datetime.datetime.today().date())
    date_end = models.DateField("дата окончани", default=datetime.date.today() + relativedelta(months=1))

    class Meta():
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
