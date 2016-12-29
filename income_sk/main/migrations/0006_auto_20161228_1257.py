# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161228_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fragmentname',
            name='identifier',
            field=models.CharField(default=1234, max_length=100, null=True),
        ),
    ]
