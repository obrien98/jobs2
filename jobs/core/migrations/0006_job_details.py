# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='details',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]