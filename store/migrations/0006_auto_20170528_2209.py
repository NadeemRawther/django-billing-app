# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20170528_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='Store-picture', verbose_name='Image'),
        ),
    ]