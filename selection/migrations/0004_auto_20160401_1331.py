# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_auto_20160330_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='timetable',
            field=models.IntegerField(default=0),
        ),
    ]
