# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from1', models.CharField(max_length=20)),
                ('type_of_truck', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Material_Name', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Number_Of_Truck', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=20)),
                ('Volume', models.CharField(max_length=20)),
                ('Material_Type', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]