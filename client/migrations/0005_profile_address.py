# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20170528_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=' ', verbose_name='Address'),
            preserve_default=False,
        ),
    ]
