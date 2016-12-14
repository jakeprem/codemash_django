# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_auto_20161214_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Category'),
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='rooms',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='session_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.SessionType'),
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='tags',
        ),
        migrations.AddField(
            model_name='meeting',
            name='rooms',
            field=models.ManyToManyField(to='meetings.Room'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='tags',
            field=models.ManyToManyField(to='meetings.Tag'),
        ),
    ]
