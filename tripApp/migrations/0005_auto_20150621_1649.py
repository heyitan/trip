# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tripApp', '0004_resort_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='resort',
            name='city',
            field=models.CharField(default=b'null', max_length=100),
        ),
        migrations.AddField(
            model_name='resort',
            name='country',
            field=models.CharField(default=b'null', max_length=100),
        ),
        migrations.AlterField(
            model_name='resort',
            name='hour_estimate',
            field=models.FloatField(default=1, help_text=b'How many hours would this point of interest would take? (0.5, 3. etc)'),
        ),
        migrations.AlterField(
            model_name='resort',
            name='rate_star',
            field=models.FloatField(default=5, help_text=b'Rate how much you recommend traveller to go, from 0 - 5, you could do 4.7 as well', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='resort',
            name='ticket_price',
            field=models.FloatField(default=0, help_text=b'Unit in YUAN, could translate into other currency in frontend'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
