# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=20)),
                ('grades', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('sid',),
            },
        ),
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('courses', models.ManyToManyField(to='selection.course')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sid', models.CharField(max_length=12)),
                ('cla', models.CharField(max_length=10)),
                ('courses', models.ManyToManyField(to='selection.course')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sid',),
            },
        ),
    ]
