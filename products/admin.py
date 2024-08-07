from django.contrib import admin
from .models import Product, Category, Brand, Review, ProductImages
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
