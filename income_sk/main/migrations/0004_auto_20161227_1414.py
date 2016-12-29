# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161227_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingninja',
            name='img1',
            field=models.CharField(default=b'NULL', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='codingninja',
            name='img2',
            field=models.CharField(default=b'NULL', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='codingninja',
            name='img3',
            field=models.CharField(default=b'NULL', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='codingninja',
            name='knowmore',
            field=models.CharField(default=b'NULL', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='fragmentname',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
