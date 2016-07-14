from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from Meniu.models import Menu
# Create your models here.
STATUS_CHOICES = (
    (0, "Pending"),
    (1, "Sent"),
    (2, "Finalized")
)

class Order(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length = 15)
    adress = models.CharField(max_length = 200)
    id_menu = models.ForeignKey(Menu)
    rating = models.FloatField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __unicode__(self):
        return self.name
