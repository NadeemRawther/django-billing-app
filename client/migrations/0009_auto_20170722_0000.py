# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20170705_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(default='', verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=254, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=254, verbose_name='Last Name'),
        ),
    ]