# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-17 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20171027_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='establishment_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]