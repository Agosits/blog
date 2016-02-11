# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('author', models.CharField(max_length=100, default='foobar')),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('maxid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('journals', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='journal',
            name='tags',
            field=models.CharField(max_length=1000, default=''),
        ),
        migrations.AlterField(
            model_name='journal',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='journal',
            name='time',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
