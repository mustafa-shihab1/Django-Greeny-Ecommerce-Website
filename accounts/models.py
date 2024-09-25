from django.db import models
from products.models import Product
from settings.models import Country, City
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("User"), related_name='Profile', on_delete= models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='profile/', null=True, blank=True)
    code = models.CharField(_("Code"),default=generate_code, max_length=8)
    code_used = models.BooleanField(_("Code used"), default=False)
    favourites = models.ManyToManyField(Product, verbose_name=_("Favourites"), related_name="favourite_product", null=True, blank=True)

    def __str__(self):
        return self.user.username


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
    user = models.ForeignKey(User,verbose_name=_("User"), related_name='UserPhone', on_delete= models.CASCADE)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    type = models.CharField(_("Type"),max_length=10, choices=DATA_TYPE)

    def __str__(self):
        return f"{self.user.username} - {self.type}"



class UserAddress(models.Model):
    user = models.ForeignKey(User,verbose_name=_("User"), related_name='UserAddress', on_delete= models.CASCADE)
    type = models.CharField(_("Type"), max_length=10, choices=DATA_TYPE)
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.SET_NULL, related_name='user_country', null= True)
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.SET_NULL, related_name='user_city', null= True)
    state = models.CharField(_("State"), max_length=50)
    region = models.CharField(_("Region"), max_length=50)
    street = models.CharField(_("Street"), max_length=50)
    notes = models.TextField(_("Notes"), max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"
    