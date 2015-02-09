# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accesorios', '0003_auto_20150205_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaleco',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 19, 51, 50, 235357, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collar',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 19, 51, 56, 969649, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='correa',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 19, 52, 3, 815776, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pechera',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 19, 52, 13, 944814, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
