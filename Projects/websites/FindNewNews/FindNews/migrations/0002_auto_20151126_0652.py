# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindNews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsearches',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='google_gl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='googlehost',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
