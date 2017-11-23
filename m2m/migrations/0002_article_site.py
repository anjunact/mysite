# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('m2m', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
