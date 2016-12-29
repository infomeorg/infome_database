# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161227_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='organisations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
                ('img1', models.CharField(default=b'NULL', max_length=250)),
                ('img2', models.CharField(default=b'NULL', max_length=250)),
                ('img3', models.CharField(default=b'NULL', max_length=250)),
                ('description', models.CharField(default=b'NULL', max_length=250)),
                ('knowmore', models.CharField(default=b'NULL', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='codingninja',
            name='name',
        ),
        migrations.DeleteModel(
            name='codingninja',
        ),
        migrations.RemoveField(
            model_name='mall',
            name='name',
        ),
        migrations.DeleteModel(
            name='mall',
        ),
    ]
