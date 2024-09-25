from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Country(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
    


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.CASCADE, related_name='country_city')
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='company/')
    about = models.CharField(_("About"), max_length=300)
    fb_link = models.URLField(_("Facebook Link"), blank=True, null=True)
    tw_link = models.URLField(_("Twitter Link"), blank=True, null=True)
    ins_link = models.URLField(_("Instagram Link"), blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=30)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    address = models.CharField(_("Address"), max_length=100)

    def __str__(self):
        return self.name
    