# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 22:58
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
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('establishment_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employer')),
            ],
        ),
    ]
