# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0013_schedule_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='active',
            field=models.BooleanField(),
        ),
    ]
