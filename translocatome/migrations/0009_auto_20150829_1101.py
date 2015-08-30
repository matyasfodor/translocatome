# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0008_auto_20150823_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='base_activity',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='base_concentration',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='cancer_driver',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='cancer_indirect_driver',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
