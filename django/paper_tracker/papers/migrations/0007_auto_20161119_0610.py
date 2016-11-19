# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0006_auto_20161118_2328'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collectionpapers',
            unique_together=set([('paper', 'collection')]),
        ),
    ]
