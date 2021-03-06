# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20161214_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('gravatar_url', models.URLField()),
                ('biography', models.TextField()),
                ('blog_link', models.URLField()),
                ('github_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
            ],
        ),
    ]
