# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tripApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resort_name', models.CharField(max_length=100)),
                ('resort_type', models.CharField(max_length=50)),
                ('hour_estimate', models.FloatField(default=1)),
                ('good_season', models.CharField(max_length=100)),
                ('ticket_price', models.FloatField(default=0)),
                ('rate_star', models.FloatField(default=5)),
            ],
        ),
    ]
