from django.db import models

# Create your models here.

class Collaborator(models.Model):
    email = models.EmailField('Email', primary_key=True, default=None)

    def __str__(self):
        return self.email

class Cooperation(models.Model):
    firstname = models.CharField('Name', max_length=50)
    email = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    comment = models.TextField('Comment')

    def __str__(self):
        return self.firstname