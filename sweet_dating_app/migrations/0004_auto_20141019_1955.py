# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_dating_app', '0003_auto_20141019_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='user_photo',
            field=models.ImageField(upload_to=b'user_photos'),
        ),
    ]
