# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20161214_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='room',
            field=models.CharField(max_length=200, null=True),
        ),
    ]