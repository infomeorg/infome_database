# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161227_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fragmentname',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
