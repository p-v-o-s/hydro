# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('_lat', models.DecimalField(decimal_places=9, max_digits=12)),
                ('_lng', models.DecimalField(decimal_places=9, max_digits=12)),
                ('extra', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.Device')),
            ],
        ),
    ]
