# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField()),
                ('boton_comprar', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
