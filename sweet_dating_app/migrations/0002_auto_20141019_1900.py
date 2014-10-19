# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_dating_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='user_photo',
            field=models.ImageField(null=True, upload_to=b'user_photos', blank=True),
        ),
    ]
