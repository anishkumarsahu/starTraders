# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-01-13 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankdetails',
            options={'verbose_name_plural': 'c) Bank Details'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'h) Category List'},
        ),
        migrations.AlterModelOptions(
            name='companyprofile',
            options={'verbose_name_plural': 'b) Company Profile'},
        ),
        migrations.AlterModelOptions(
            name='companyuser',
            options={'verbose_name_plural': 'm) Company User List'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'e) Customers List'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name_plural': 'l) Expense List'},
        ),
        migrations.AlterModelOptions(
            name='hsn',
            options={'verbose_name_plural': 'g) HSN List'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name_plural': 'd) Invoice'},
        ),
        migrations.AlterModelOptions(
            name='printersetting',
            options={'verbose_name_plural': 'a) Printer Setting'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'k) Product List'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name_plural': 'n) Purchase List'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'o) Sales List'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name_plural': 'f) Supplier List'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': 'j) Unit List'},
        ),
        migrations.AlterModelOptions(
            name='userprintersetting',
            options={'verbose_name_plural': 'p) User Printer Setting List'},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name_plural': 'i) Ware House List'},
        ),
        migrations.AddField(
            model_name='product',
            name='warningStockLimit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='buyersOrderNumber',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='deliveryNote',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='destination',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='dispatchDocumentNumber',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='dispatchNoteDate',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='dispatchThrough',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='otherCharges',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='otherReference',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='roundOff',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierReference',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='paidAgainstBill',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='customerID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Customer'),
        ),
    ]
