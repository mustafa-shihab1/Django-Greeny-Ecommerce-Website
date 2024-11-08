# Generated by Django 5.0.7 on 2024-09-14 16:35

import django.db.models.deletion
import django.utils.timezone
import utils.generate_code
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_user'),
        ('products', '0013_product_video_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=utils.generate_code.generate_code, max_length=8, verbose_name='Code')),
                ('order_status', models.CharField(choices=[('Inprogress', 'Inprogress'), ('Completed', 'Completed')], max_length=10, verbose_name='Order Status')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Order Time')),
                ('delivery_time', models.DateTimeField(blank=True, null=True, verbose_name='Delivery Time')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_cart', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('price', models.FloatField(verbose_name='Price')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_product', to='products.product', verbose_name='Product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_detail', to='orders.cartorder', verbose_name='Order')),
            ],
        ),
    ]
