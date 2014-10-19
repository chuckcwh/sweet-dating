# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_dating_app', '0004_auto_20141019_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='user_photo2',
        ),
    ]
