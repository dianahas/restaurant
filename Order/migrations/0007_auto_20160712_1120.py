# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_auto_20160712_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Sent')], default=0),
        ),
    ]
