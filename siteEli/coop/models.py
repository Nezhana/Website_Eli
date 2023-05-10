from django.db import models

# Create your models here.

class Cooperation(models.Model):
    firstname = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    comment = models.TextField('Comment')

    def __str__(self):
        return self.firstname