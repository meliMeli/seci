# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeseries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='location',
            name='region_code',
        ),
        migrations.RemoveField(
            model_name='location',
            name='target_type',
        ),
        migrations.AlterField(
            model_name='monthaggregationdata',
            name='event_type',
            field=models.IntegerField(choices=[(1, 'Violent crime'), (2, 'Murder'), (3, 'Forcible rape'), (4, 'Robbery')]),
        ),
        migrations.AlterField(
            model_name='monthaggregationdata',
            name='events',
            field=models.IntegerField(default=0),
        ),
    ]
