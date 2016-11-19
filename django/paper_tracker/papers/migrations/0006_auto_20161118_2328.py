# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20161118_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='publication',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
