# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0006_auto_20160401_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='classromm',
            field=models.CharField(max_length=10, default='0-000'),
        ),
    ]
