from django.db import models

# Create your models here.

class Song(models.Model):
    author = models.CharField('Song author', max_length=50)
    title = models.CharField('Song name', max_length=50)
    song = models.FileField('Song file', upload_to='songs/', help_text='.mp3 supported only')

    def __str__(self):
        return self.title