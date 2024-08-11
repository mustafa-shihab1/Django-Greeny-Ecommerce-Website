from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Country(models.Model):
    name = models.CharField(_("Country"), max_length=50)

    def __str__(self):
        return self.name
    

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_city')
    name = models.CharField(_("City"), max_length=50)

    def __str__(self):
        return self.name