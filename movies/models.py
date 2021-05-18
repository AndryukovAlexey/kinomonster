from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Movies(models.Model):
    title = models.CharField("Название", max_length=70)
    movie = models.URLField("Кино")
    year = models.IntegerField("Дата выхода")
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    author =  models.CharField("Режиссер", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("изображение", default='', upload_to='films/')
    
    class Meta():
        verbose_name = 'кино'
        verbose_name_plural = 'фильмы'

class Serials(models.Model):
    title = models.CharField("Название", max_length=70)
    movie = models.URLField("Сериал")
    year = models.IntegerField("Дата выхода")
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    author =  models.CharField("Режиссер", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("изображение", default='', upload_to='serials/')
    
    class Meta():
        verbose_name = 'сериал'
        verbose_name_plural = 'сериалы'
#movie = models.ForeignKey(Movies, default=None, on_delete=models.CASCADE)
class News(models.Model):
    date = models.DateTimeField("дата", default=timezone.now)
    text = models.CharField('Текст', max_length=100)

    class Meta():
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Comments(models.Model):
    movie = models.ForeignKey(Movies, null=True, on_delete=models.CASCADE)
    serial = models.ForeignKey(Serials, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatars-comm/')
    text = models.TextField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Likes(models.Model):
    name = models.CharField('Название', default='', max_length=70)
    movie = models.ForeignKey(Movies, null=True, on_delete=models.CASCADE)
    serial = models.ForeignKey(Serials, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"


