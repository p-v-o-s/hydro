# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_remove_device_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
