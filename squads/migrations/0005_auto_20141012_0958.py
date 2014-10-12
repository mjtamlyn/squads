# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0004_auto_20141012_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sessionsection',
            name='time',
            field=models.PositiveIntegerField(verbose_name=b'Time (in minutes)'),
        ),
    ]
