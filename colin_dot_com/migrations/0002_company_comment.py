# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colin_dot_com', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='comment',
            field=models.CharField(default='hehehe', max_length=400),
            preserve_default=False,
        ),
    ]
