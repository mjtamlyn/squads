# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0003_auto_20141012_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingtype',
            name='category',
            field=models.ForeignKey(default=1, to='squads.TrainingCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sessionsection',
            name='time',
            field=models.PositiveIntegerField(),
        ),
    ]
