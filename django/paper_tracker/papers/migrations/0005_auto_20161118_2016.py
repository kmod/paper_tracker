# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_auto_20161114_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionpapers',
            name='read',
        ),
        migrations.AddField(
            model_name='collectionpapers',
            name='intro_conclusion_read',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='collectionpapers',
            name='paper_read',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='collectionpapers',
            name='refs_expanded',
            field=models.BooleanField(default=0),
        ),
    ]
