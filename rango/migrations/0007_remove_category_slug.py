# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20170203_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
