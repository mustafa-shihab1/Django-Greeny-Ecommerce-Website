from django.db import models
from settings.models import Country, City
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='Profile', on_delete= models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)


# create user -----> create profile
# sender: user   -  instance: data from user   -   created: boolean only TRUE in case of signup   -  action-> create profile
# when django user (created) and (saved), the 'create_profile' function will be called and create new profile for that user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created,**kewargs):
    if created:
        Profile.objects.create( user = instance )

DATA_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Academy','Academy'),
    ('Others','Others'),
)


class UserPhoneNumber(models.Model):
    user = models.OneToOneField(User, related_name='UserPhone', on_delete= models.CASCADE)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=10, choices=DATA_TYPE)


class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='UserAddress', on_delete= models.CASCADE)
    type = models.CharField(max_length=10, choices=DATA_TYPE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name='user_country', null= True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='user_city', null= True)
    state = models.CharField(_("State"), max_length=50)
    region = models.CharField(_("Region"), max_length=50)
    street = models.CharField(_("Street"), max_length=50)
    notes = models.TextField(_("Notes"), max_length=300, blank=True, null=True)