# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-22 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farzand_Parvari_app', '0009_star_table_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star_table',
            name='Date_Time',
            field=models.DateField(),
        ),
    ]
