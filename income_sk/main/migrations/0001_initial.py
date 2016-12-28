# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='codingninja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img1', models.CharField(max_length=250)),
                ('img2', models.CharField(max_length=250)),
                ('img3', models.CharField(max_length=250)),
                ('knowmore', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fragmentname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img1', models.CharField(default=b'NULL', max_length=250)),
                ('img2', models.CharField(default=b'NULL', max_length=250)),
                ('img3', models.CharField(default=b'NULL', max_length=250)),
                ('knowmore', models.CharField(default=b'NULL', max_length=1000)),
                ('name', models.ForeignKey(to='main.fragmentname')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='codingninja',
            name='name',
            field=models.ForeignKey(to='main.fragmentname'),
            preserve_default=True,
        ),
    ]
