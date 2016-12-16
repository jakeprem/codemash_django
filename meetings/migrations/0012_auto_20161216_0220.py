# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0011_auto_20161215_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(unique=True)),
                ('end_datetime', models.DateTimeField()),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Schedule')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='meetings',
            field=models.ManyToManyField(through='meetings.ScheduleMeeting', to='meetings.Meeting'),
        ),
    ]