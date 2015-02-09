# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juguetes', '0002_pelota_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelota',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 19, 52, 20, 453905, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
