# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-12-22 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_expense_companyid'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='dueOrReturnAmount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='sales',
            name='paidAmount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='salesproduct',
            name='unit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
