# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rawscanresult_scan_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanerror',
            name='scan_host',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
