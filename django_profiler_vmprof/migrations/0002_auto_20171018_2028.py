# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-18 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_profiler_vmprof', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestprofile',
            name='allocated_vm',
            field=models.BigIntegerField(),
        ),
    ]
