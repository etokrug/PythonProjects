# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkUrls',
            fields=[
                ('pk_linkurls_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('base_url', models.CharField(db_index=True, max_length=400)),
                ('path_url', models.CharField(db_index=True, max_length=1600)),
                ('country', models.CharField(null=True, max_length=300)),
                ('date_first_searched', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pk_project_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('project_name', models.CharField(db_index=True, max_length=255)),
                ('project_description', models.CharField(max_length=8000)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False, null=True)),
                ('fk_p_user_created', models.ForeignKey(related_name='fk_p_user_created', to=settings.AUTH_USER_MODEL, null=True)),
                ('fk_p_user_updated', models.ForeignKey(related_name='fk_p_user_updated', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSearches',
            fields=[
                ('pk_projectsearches_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=300)),
                ('search_terms', models.CharField(max_length=1000)),
                ('language', models.CharField(null=True, max_length=50)),
                ('exact_terms', models.CharField(null=True, max_length=1000)),
                ('exclude_terms', models.CharField(null=True, max_length=1000)),
                ('date_restrict', models.DateTimeField(null=True)),
                ('search_time', models.FloatField(null=True)),
                ('total_results', models.IntegerField(null=True)),
                ('search_date', models.DateTimeField(editable=False)),
                ('updated_date', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SearchEngines',
            fields=[
                ('pk_searchengines_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('search_name', models.CharField(db_index=True, max_length=150)),
                ('search_site', models.CharField(max_length=300)),
                ('search_api', models.CharField(max_length=300)),
                ('search_key', models.CharField(max_length=300)),
                ('api_key', models.CharField(max_length=300)),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_updated', models.DateTimeField(editable=False)),
                ('fk_se_user_created', models.ForeignKey(related_name='fk_se_user_created', to=settings.AUTH_USER_MODEL, null=True)),
                ('fk_se_user_updated', models.ForeignKey(related_name='fk_se_user_updated', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('pk_searchresults_id', models.AutoField(primary_key=True, editable=False, serialize=False)),
                ('title', models.CharField(null=True, db_index=True, max_length=500)),
                ('snippet', models.CharField(null=True, max_length=8000)),
                ('page_map', models.CharField(null=True, max_length=8000)),
                ('fk_linkurls', models.ForeignKey(to='FindNews.LinkUrls')),
                ('fk_projectsearches', models.ForeignKey(to='FindNews.ProjectSearches')),
            ],
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='fk_engine',
            field=models.ForeignKey(to='FindNews.SearchEngines'),
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='fk_project',
            field=models.ForeignKey(to='FindNews.Project'),
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='fk_ps_user_created',
            field=models.ForeignKey(related_name='fk_ps_user_created', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='projectsearches',
            name='fk_ps_user_updated',
            field=models.ForeignKey(related_name='fk_ps_user_updated', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
