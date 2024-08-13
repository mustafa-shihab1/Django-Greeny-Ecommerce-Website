# Generated by Django 5.0.7 on 2024-08-11 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAddress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userphonenumber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPhone', to=settings.AUTH_USER_MODEL),
        ),
    ]