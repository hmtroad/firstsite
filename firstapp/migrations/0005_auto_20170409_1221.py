# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-09 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20170408_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='major',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]