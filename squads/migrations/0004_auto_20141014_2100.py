# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0003_coachnote_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coachnote',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='sessionlog',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='video',
            name='notes',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coachnote',
            name='content',
            field=models.TextField(verbose_name=b'Message'),
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=embed_video.fields.EmbedVideoField(verbose_name=b'Youtube link'),
        ),
    ]
