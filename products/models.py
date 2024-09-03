from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

FLAG_TYPE = (
    ('New', 'New'),
    ('Feature', 'Feature'),
)

class ProductQueryset(models.QuerySet):
    def price_greater_than(self,price):
        return self.filter(price__gt=price)
    

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)
    
    def price_greater_than(self,price):
        return self.get_queryset().price_greater_than(price)

# USE -> In views.py: queryset = Product.objects.price_greater_than(30)  

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
    image = models.ImageField(_("Image"), upload_to='Product/')
    quantity = models.IntegerField(_("Quantity"), default=0)

    # class Meta:
    #     order_by = 'name'
    objects = ProductManager()

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # instance method
    def get_absolute_url(self):
        #   url 'base-url:sub-url' filed-name
        return reverse('products:product_detail', kwargs={'slug': self.slug})
    
    
    def __str__(self):
       return self.name
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='products/')
    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='brand/')
    slug = models.SlugField(_("Slug"), null=True, blank= True)

    # when create any new brand it will create/save a new slug for it 
    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

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