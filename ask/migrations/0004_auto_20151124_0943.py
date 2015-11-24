# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_auto_20151123_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bank_account',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
