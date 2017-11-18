# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170728_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='profession',
            name='spec_4',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='spec_5',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='spec_6',
        ),
        migrations.AddField(
            model_name='city',
            name='region_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Region'),
        ),
        migrations.AddField(
            model_name='university',
            name='region_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Region'),
        ),
    ]
