# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0007_auto_20161214_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='abstract',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='session_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]