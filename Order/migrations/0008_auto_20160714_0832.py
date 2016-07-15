# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_auto_20160712_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Sent'), (2, 'Finalized')], default=0),
        ),
    ]