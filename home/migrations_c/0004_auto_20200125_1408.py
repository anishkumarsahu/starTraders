# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-01-25 14:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20200125_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Q) Payment History List',
            },
        ),
        migrations.CreateModel(
            name='SalesLater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(blank=True, max_length=200, null=True)),
                ('customerGst', models.CharField(blank=True, max_length=200, null=True)),
                ('customerPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('customerEmail', models.CharField(blank=True, max_length=200, null=True)),
                ('customerAddress', models.CharField(blank=True, max_length=500, null=True)),
                ('customerState', models.CharField(blank=True, max_length=200, null=True)),
                ('salesType', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=200, null=True)),
                ('creditDays', models.IntegerField(default=0)),
                ('invoiceNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('invoiceDate', models.DateField(blank=True, null=True)),
                ('subTotal', models.FloatField(default=0.0)),
                ('taxable', models.FloatField(default=0.0)),
                ('totalFinal', models.FloatField(default=0.0)),
                ('billDisc', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('grandTotal', models.FloatField(default=0.0)),
                ('roundOff', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('paidDate', models.DateField(blank=True, null=True)),
                ('chequeDetail', models.CharField(blank=True, max_length=500, null=True)),
                ('deliveryNote', models.CharField(blank=True, max_length=500, null=True)),
                ('supplierReference', models.CharField(blank=True, max_length=500, null=True)),
                ('buyersOrderNumber', models.CharField(blank=True, max_length=500, null=True)),
                ('dispatchDocumentNumber', models.CharField(blank=True, max_length=500, null=True)),
                ('dispatchThrough', models.CharField(blank=True, max_length=500, null=True)),
                ('otherReference', models.CharField(blank=True, max_length=500, null=True)),
                ('dispatchNoteDate', models.CharField(blank=True, max_length=500, null=True)),
                ('destination', models.CharField(blank=True, max_length=500, null=True)),
                ('otherCharges', models.FloatField(default=0.0)),
                ('paidAmount', models.FloatField(default=0.0)),
                ('dueOrReturnAmount', models.FloatField(default=0.0)),
                ('invoiceActualNumber', models.IntegerField(default=0)),
                ('paidAgainstBill', models.FloatField(default=0.0)),
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
                ('customerID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Customer')),
                ('invoiceSeriesID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Invoice')),
            ],
            options={
                'verbose_name_plural': 'R) Booking List',
            },
        ),
        migrations.CreateModel(
            name='SalesLaterProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('hsn', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(blank=True, max_length=200, null=True)),
                ('rate', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('disc', models.FloatField(default=0.0)),
                ('netRate', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
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
        migrations.AddField(
            model_name='saleslaterproduct',
            name='productID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AddField(
            model_name='saleslaterproduct',
            name='salesID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.SalesLater'),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='salesID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Sales'),
        ),
    ]
