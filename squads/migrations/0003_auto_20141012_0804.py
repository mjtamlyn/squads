# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20141012_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionsection',
            name='notes',
        ),
        migrations.AlterField(
            model_name='sessionsection',
            name='time',
            field=models.PositiveIntegerField(help_text=b'in minutes'),
        ),
    ]
