# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_dating_app', '0002_auto_20141019_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='id',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
