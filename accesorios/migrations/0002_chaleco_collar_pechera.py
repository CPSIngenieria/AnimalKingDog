# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesorios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaleco',
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
        migrations.CreateModel(
            name='Collar',
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
        migrations.CreateModel(
            name='Pechera',
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
