# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_auto_20151123_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='completed_polls',
            field=models.ManyToManyField(to='ask.Poll', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('poll', 'question', 'answer')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('poll', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together=set([('user', 'poll', 'question', 'answer')]),
        ),
    ]
