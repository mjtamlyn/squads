# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0004_auto_20141014_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='squad',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='trainingcategory',
            options={'ordering': ['pk'], 'verbose_name_plural': 'training categories'},
        ),
        migrations.AlterModelOptions(
            name='trainingtype',
            options={'ordering': ['pk']},
        ),
    ]
