# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripApp', '0002_resort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='good_season',
            field=models.CharField(max_length=2, choices=[(b'SP', b'Spring'), (b'SU', b'Summer'), (b'AU', b'Autumn'), (b'WI', b'Winter')]),
        ),
        migrations.AlterField(
            model_name='resort',
            name='resort_type',
            field=models.CharField(max_length=3, choices=[(b'HIS', b'History'), (b'VIW', b'View'), (b'ACT', b'Activity'), (b'CUL', b'Culter')]),
        ),
    ]
