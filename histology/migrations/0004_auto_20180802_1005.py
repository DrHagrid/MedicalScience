# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-02 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('histology', '0003_auto_20180802_0947'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SampleSection',
            new_name='SampleType',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='section',
            new_name='type',
        ),
    ]
