# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20160711_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
