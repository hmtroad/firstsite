# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-24 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20170410_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_name', models.CharField(blank=True, max_length=200, null=True)),
                ('act_address', models.CharField(blank=True, max_length=200, null=True)),
                ('introduction', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(blank=True, max_length=200, null=True)),
                ('assoc', models.CharField(blank=True, max_length=200, null=True)),
                ('apply_time', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asc_name', models.CharField(blank=True, max_length=200, null=True)),
                ('asc_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepter', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MememberOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=200, null=True)),
                ('assoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('writer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='people',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mememberof',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.People'),
        ),
        migrations.AddField(
            model_name='inform',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.People'),
        ),
        migrations.AddField(
            model_name='activity',
            name='hoster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Association'),
        ),
    ]