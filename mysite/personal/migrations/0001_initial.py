# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('from1', models.CharField(max_length=20)),
                ('type_of_truck', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Material_Name', models.CharField(max_length=20)),
                ('To', models.CharField(max_length=20)),
                ('Number_Of_Truck', models.CharField(max_length=20)),
                ('Time', models.TimeField()),
                ('Volume', models.CharField(max_length=20)),
                ('Material_Type', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
            options={
                'ordering': ['-timestamp', '-Time'],
            },
        ),
    ]
