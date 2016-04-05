# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0007_course_classromm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='classromm',
            new_name='classroom',
        ),
    ]
