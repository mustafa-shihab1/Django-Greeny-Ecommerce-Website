from django.contrib import admin
from .models import Product, Category, Brand, Review, ProductImages
from django_summernote.admin import SummernoteModelAdmin
from django.db.models.aggregates import Avg

# Register your models here.


class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'
    list_per_page = 50
    list_display = ['name','category','brand','review_count','rate_avg']

    def review_count(self,obj):
        return obj.product_review.count()
    
    def rate_avg(self,obj):
        avg = obj.product_review.aggregate(myAvg=Avg('rate'))
        return avg['myAvg']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
