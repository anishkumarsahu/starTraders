# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-12-26 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accHolderName', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bankName', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('accNo', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('branch', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('accountType', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('ifsc', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('bankAddress', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('brand', models.CharField(blank=True, default='N/A', max_length=200, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('gst', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('zip', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('email', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('userPassword', models.CharField(blank=True, max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('company_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
                ('user_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('gst', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('email', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseType', models.CharField(default='N/A', max_length=200)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('expenseDate', models.DateField(blank=True, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Hsn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('tax', models.FloatField(default=0.0)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceSeries', models.CharField(max_length=100)),
                ('invoiceMaxCount', models.IntegerField(default=1000)),
                ('invoiceStartWith', models.IntegerField(default=1)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('isCompleted', models.BooleanField(default=False)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PrinterSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('brand', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mrp', models.FloatField(default=0.0)),
                ('cost', models.FloatField(default=0.0)),
                ('spWithoutGst', models.FloatField(default=0.0)),
                ('spWithGst', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('discountPc', models.FloatField(default=0.0)),
                ('barcode', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('productType', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('categoryID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
                ('company_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierName', models.CharField(blank=True, max_length=200, null=True)),
                ('supplierGst', models.CharField(blank=True, max_length=200, null=True)),
                ('supplierPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('supplierEmail', models.CharField(blank=True, max_length=200, null=True)),
                ('supplierAddress', models.CharField(blank=True, max_length=500, null=True)),
                ('supplierState', models.CharField(blank=True, max_length=200, null=True)),
                ('purchaseType', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentType', models.CharField(blank=True, max_length=200, null=True)),
                ('creditDays', models.IntegerField(default=0)),
                ('invoiceNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('invoiceDate', models.DateField(blank=True, null=True)),
                ('taxable', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('paidDate', models.DateField(blank=True, null=True)),
                ('chequeDetail', models.CharField(blank=True, max_length=500, null=True)),
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('hsn', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(blank=True, max_length=200, null=True)),
                ('rate', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0.0)),
                ('netRate', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('productID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
                ('purchaseID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
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
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SalesProduct',
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
                ('productID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
                ('salesID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Sales')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('gst', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('email', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPrinterSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printerID', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.PrinterSetting')),
                ('userID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wareHouseName', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('wareHouseAddress', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='customerID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Supplier'),
        ),
        migrations.AddField(
            model_name='sales',
            name='invoiceSeriesID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Invoice'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplierID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='unitID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Unit'),
        ),
        migrations.AddField(
            model_name='product',
            name='wareHouse_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.WareHouse'),
        ),
        migrations.AddField(
            model_name='category',
            name='hsnID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Hsn'),
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='companyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CompanyProfile'),
        ),
    ]