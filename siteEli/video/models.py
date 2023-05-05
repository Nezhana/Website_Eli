from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField('Назва', max_length=50)
    desc = models.TextField('Опис')
    text = models.CharField('Текст', max_length=50, default='Eli')
    music = models.CharField('Музичний супровід', max_length=50, default='Eli')
    vocal = models.CharField('Вокал', max_length=50, default='Eli')
    img = models.CharField('Превью', max_length=12)
    link = models.CharField('Посилання', max_length=250)

    def __str__(self):
        return self.title