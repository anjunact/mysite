# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_ip',
            name='ip',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='t_ip',
            name='port',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]