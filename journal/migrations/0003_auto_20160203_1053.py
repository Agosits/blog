# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20160202_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='time',
            field=models.DateField(max_length=1000),
        ),
    ]
