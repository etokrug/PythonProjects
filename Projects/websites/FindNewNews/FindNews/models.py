from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Project(models.Model):
    pk_project_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_user_id_created = models.ForeignKey(User, related_name='project_user_id_created', null=False)
    project_name = models.CharField(db_index=True, null=False, max_length=255)
    # TODO: Implement fulltext indext in DB Table project
    project_description = models.CharField(max_length=8000)
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=True, editable=False)
    fk_user_id_updated = models.ForeignKey(User, related_name='project_user_id_updated', null=False)

    def save(self):
        if not self.pk_project_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        super(Project, self).save()

    #Reference
    #http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/

class SearchEngines(models.Model):
    pk_searchengines_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_user_id_created = models.ForeignKey(User, related_name='searchengines_user_id_created', null=False)
    # The name given to this search either on the site OR just for these purposes
    search_name = models.CharField(db_index=True, null=False, max_length=150)
    # This would be like "google.com"
    search_site = models.CharField(null=False, max_length=300)
    # This would be the api used like google custom search/google site search/bing etc
    search_api = models.CharField(max_length=300)
    # The key needed/issued to access the api
    search_key = models.CharField(max_length=300)
    # The api key if you need to register an app with the site
    api_key = models.CharField(max_length=300)
    # The initial date it was created
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=False, editable=False)
    fk_user_id_updated = models.ForeignKey(User, 'searchengines_user_id_updated', null=False)

    def save(self):
        if not self.pk_searchengines_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        super(SearchEngines, self).save()


class ProjectSearches(models.Model):
    pk_projectsearches_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_project_id = models.ForeignKey(Project, null=False)
    fk_engine_id = models.ForeignKey(SearchEngines, null=False)
    fk_user_id_created = models.ForeignKey(User, related_name='projectsearches_user_id_created', null=False)
    title = models.CharField(db_index=True, null=False, max_length=300)
    # TODO: Implement fulltext indext in DB Table projectsearches
    # This should take space delimited input
    search_terms = models.CharField(null=False, max_length=1000)
    language = models.CharField(null=True, max_length=50)
    # This should take space delimited input
    exact_terms = models.CharField(null=True, max_length=1000)
    # This should take space delimited input
    exclude_terms = models.CharField(null=True, max_length=1000)
    date_restrict = models.DateTimeField(null=True)
    # This should be the search time returned on the first extract returned by the search
    search_time = models.FloatField(null=True)
    total_results = models.IntegerField(null=True)
    # Date the initial search was run
    search_date = models.DateTimeField(null=False, editable=False)
    updated_date = models.DateTimeField(null=False, editable=False)
    fk_user_id_updated = models.ForeignKey(User, related_name='projectsearches_user_id_updated', null=False)

    def save(self):
        if not self.pk_projectsearches_id:
            self.search_date = timezone.now()
        self.updated_date = timezone.now()


class LinkUrls(models.Model):
    pk_linkurls_id = models.AutoField(null=False, primary_key=True, editable=False)
    # TODO: In view use "from urllib.parse import urlparse" to implement splitting of URL
    # https://docs.python.org/2/library/urlparse.html
    # base_url and path_url are implemented to have a total possible size of 2000
    # https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers/417184#417184
    base_url = models.CharField(db_index=True, null=False, max_length=400)
    path_url = models.CharField(db_index=True, null=False, max_length=1600)
    country = models.CharField(null=True, max_length=300)
    date_first_searched = models.DateTimeField(null=False, editable=False)

    def save(self):
        if not self.pk_linkurls_id:
            self.date_first_searched = timezone.now()


class SearchResults(models.Model):
    pk_searchresults_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_projectsearches_id = models.ForeignKey(ProjectSearches, null=False)
    fk_linkurls_id = models.ForeignKey(LinkUrls, null=False)
    title = models.CharField(db_index=True, null=True, max_length=500)
    # TODO: Implement fulltext index in DB
    snippet = models.CharField(null=True, max_length=8000)
    page_map = models.CharField(null=True, max_length=8000)












