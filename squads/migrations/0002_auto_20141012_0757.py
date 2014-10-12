# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainingcategory',
            options={'verbose_name_plural': 'training categories'},
        ),
        migrations.AddField(
            model_name='sessionlog',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
