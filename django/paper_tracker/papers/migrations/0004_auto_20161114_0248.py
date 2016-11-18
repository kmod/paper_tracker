# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_auto_20161107_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
