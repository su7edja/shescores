# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_auto_20170122_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]