# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-02-07 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200125_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='personalDiscount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='saleslater',
            name='personalDiscount',
            field=models.FloatField(default=0.0),
        ),
    ]
