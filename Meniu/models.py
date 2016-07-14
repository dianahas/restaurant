from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length = 200)
    datta = models.DateField('date published')
    fel1 = models.CharField(max_length = 200)
    fel2 = models.CharField(max_length = 200)
    desert = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.title