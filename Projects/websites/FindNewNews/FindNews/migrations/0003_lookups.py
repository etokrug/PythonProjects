# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FindNews', '0002_auto_20151126_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookUps',
            fields=[
                ('pk_lookups_id', models.AutoField(primary_key=True, serialize=False, editable=False)),
                ('variable_name', models.CharField(max_length=255, db_index=True)),
                ('display_name', models.CharField(null=True, max_length=255)),
                ('url_variable', models.CharField(max_length=255, db_index=True)),
                ('variable_description', models.CharField(null=True, max_length=1000)),
                ('deprecated_variable', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False)),
                ('fk_lu_user_created', models.ForeignKey(null=True, related_name='fk_lu_user_created', to=settings.AUTH_USER_MODEL)),
                ('fk_lu_user_updated', models.ForeignKey(null=True, related_name='fk_lu_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
