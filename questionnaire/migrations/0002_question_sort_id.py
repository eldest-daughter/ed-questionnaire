# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sort_id',
            field=models.IntegerField(help_text=b'Questions within a questionset are sorted by sort order first, question number second', null=True, blank=True),
            preserve_default=True,
        ),
    ]
