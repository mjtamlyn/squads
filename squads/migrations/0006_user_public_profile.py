# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0005_auto_20141014_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_profile',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
