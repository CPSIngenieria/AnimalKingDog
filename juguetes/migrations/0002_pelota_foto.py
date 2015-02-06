# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juguetes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelota',
            name='foto',
            field=models.ImageField(default=None, upload_to=b'fotos_pelotas'),
            preserve_default=False,
        ),
    ]
