# Generated by Django 5.0.7 on 2024-09-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='VideoUrl'),
        ),
    ]
