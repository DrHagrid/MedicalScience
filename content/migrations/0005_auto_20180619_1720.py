# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-19 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20180619_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bone',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='bones', verbose_name='Изображение'),
        ),
    ]
