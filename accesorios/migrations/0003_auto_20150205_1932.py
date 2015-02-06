# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesorios', '0002_chaleco_collar_pechera'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaleco',
            name='foto',
            field=models.ImageField(default=None, upload_to=b'fotos_chalecos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collar',
            name='foto',
            field=models.ImageField(default=None, upload_to=b'fotos_collares'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='correa',
            name='foto',
            field=models.ImageField(default=None, upload_to=b'fotos_correas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pechera',
            name='foto',
            field=models.ImageField(default=None, upload_to=b'fotos_pecheras'),
            preserve_default=False,
        ),
    ]
