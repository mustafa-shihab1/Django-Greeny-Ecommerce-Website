from django.db import models
from settings.models import Country, City
from django.utils.translation import gettext as _

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/')


DATA_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Academy','Academy'),
    ('Others','Others'),
)


class UserPhoneNumber(models.Model):
    user = ''
    phone_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=DATA_TYPE)


class UserAddress(models.Model):
    user = ''
    type = models.CharField(max_length=10, choices=DATA_TYPE)
    country = models.ForeignKey(_("Country"),Country, on_delete=models.SET_NULL, related_name='user_country', null= True)
    city = models.ForeignKey(_("City"),City, on_delete=models.SET_NULL, related_name='user_city', null= True)
    state = models.CharField(_("State"), max_length=50)
    region = models.CharField(_("Region"), max_length=50)
    street = models.CharField(_("Street"), max_length=50)
    notes = models.TextField(_("Notes"), max_length=300, blank=True, null=True)