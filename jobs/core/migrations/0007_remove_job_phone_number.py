# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_job_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='phone_number',
        ),
    ]
