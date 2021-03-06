# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-02-08 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200207_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='warningStockLimit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='purchaseproduct',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='saleslaterproduct',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='salesproduct',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
    ]
