# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20161107_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='pdf_url',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='collectionpapers',
            name='notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='collectionpapers',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
