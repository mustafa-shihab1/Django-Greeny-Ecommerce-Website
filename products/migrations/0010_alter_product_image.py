# Generated by Django 5.0.7 on 2024-08-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Product/', verbose_name='Image'),
        ),
    ]
