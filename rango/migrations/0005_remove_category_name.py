# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_category_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
