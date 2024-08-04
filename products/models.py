from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.

FLAG_TYPE = (
    ('New', 'New'),
    ('Feature', 'Feature'),
)

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey('Brand', related_name='product_brand', verbose_name=_("Brand"), on_delete=models.SET_NULL, null=True, blank= True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(_("Desc"), max_length=10000)
    tags = TaggableManager(blank=True)
    flag = models.CharField(_("Flag"), max_length=10, choices=FLAG_TYPE)
    category = models.ForeignKey('Category', related_name='product_category', verbose_name=_("Category"), on_delete=models.SET_NULL, null=True, blank= True)
    slug = models.SlugField(_("Slug"), null=True, blank= True)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
       return self.name
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='products/')
    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='category/')
    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_("User"), related_name='review_author', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product ,verbose_name=_("Product"), related_name='product_review', on_delete=models.CASCADE)
    review = models.TextField(_("Review"), max_length=500)
    rate = models.IntegerField(_("Rate"), validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
        ])
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"