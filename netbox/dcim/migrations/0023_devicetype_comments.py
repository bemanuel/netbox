# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0022_color_names_to_rgb'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicetype',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
