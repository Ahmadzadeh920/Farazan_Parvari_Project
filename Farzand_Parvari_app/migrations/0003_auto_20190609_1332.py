# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-09 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farzand_Parvari_app', '0002_remove_profilepsy_profile_image_psy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='grade_Educations',
            field=models.CharField(max_length=250),
        ),
    ]
