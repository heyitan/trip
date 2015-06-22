# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tripApp', '0003_auto_20150621_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='resort',
            name='position',
            field=geoposition.fields.GeopositionField(default=datetime.datetime(2015, 6, 21, 23, 9, 12, 832000, tzinfo=utc), max_length=42),
            preserve_default=False,
        ),
    ]
