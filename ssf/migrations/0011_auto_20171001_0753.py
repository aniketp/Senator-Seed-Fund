# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssf', '0010_adminpost_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='pin',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]