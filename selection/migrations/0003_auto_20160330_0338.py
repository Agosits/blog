# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0002_course_compulsory'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='power',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='compulsory',
            field=models.BooleanField(default='False'),
        ),
    ]
