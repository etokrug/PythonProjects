from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from FindNewNews.extras import CharNullField


class Project(models.Model):
    pk_project_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_p_user_created = models.ForeignKey(User, related_name='fk_p_user_created', null=True)
    project_name = models.CharField(db_index=True, null=False, max_length=255)
    # TODO: Implement fulltext indext in DB Table project
    project_description = CharNullField(max_length=8000, null=True, blank=True)
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=True, editable=False)
    fk_p_user_updated = models.ForeignKey(User, related_name='fk_p_user_updated', null=True)

    def save(self):
        if not self.pk_project_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        super(Project, self).save()

    def __str__(self):
        return self.project_name

    #Reference
    #http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/


class SearchEngines(models.Model):
    pk_searchengines_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_se_user_created = models.ForeignKey(User, related_name='fk_se_user_created', null=True)
    # The name given to this search either on the site OR just for these purposes
    search_name = models.CharField(db_index=True, null=False, max_length=150)
    # This would be like "google.com"
    search_site = models.CharField(null=False, max_length=300)
    # This would be the api used like google custom search/google site search/bing etc
    search_api = models.CharField(max_length=300)
    # The key needed/issued to access the api (ie custom search engine ID to use)
    search_key = models.CharField(max_length=300)
    # The api key if you need to register an app with the site
    api_key = models.CharField(max_length=300)
    # The initial date it was created
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=False, editable=False)
    fk_se_user_updated = models.ForeignKey(User, related_name='fk_se_user_updated', null=True)

    def save(self):
        if not self.pk_searchengines_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        super(SearchEngines, self).save()

    def __str__(self):
        return self.search_name


class ProjectSearches(models.Model):
    pk_projectsearches_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_project = models.ForeignKey(Project, null=False)
    fk_engine = models.ForeignKey(SearchEngines, null=False)
    fk_ps_user_created = models.ForeignKey(User, related_name='fk_ps_user_created', null=True)
    title = models.CharField(db_index=True, null=False, max_length=300)
    # TODO: Implement fulltext index in DB Table projectsearches
    # This should take space delimited input
    search_terms = models.CharField(null=False, max_length=1000)
    # language refers to lr in GCSUrlBuilder
    language = models.CharField(null=True, max_length=50)
    # country refers to cr in GCSUrlBuilder
    country = models.CharField(null=True, max_length=50)
    googlehost = models.CharField(null=True, max_length=100)
    # Refers to gl in GCSUrlBuilder
    google_gl = models.CharField(null=True, max_length=100)
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
    fk_ps_user_updated = models.ForeignKey(User, related_name='fk_ps_user_updated', null=True)

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
    fk_projectsearches = models.ForeignKey(ProjectSearches, null=False)
    fk_linkurls = models.ForeignKey(LinkUrls, null=False)
    title = models.CharField(db_index=True, null=True, max_length=500)
    # TODO: Implement fulltext index in DB
    snippet = models.CharField(null=True, max_length=8000)
    page_map = models.CharField(null=True, max_length=8000)


class LookUpVariables(models.Model):
    pk_lookupvariables_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_searchengines = models.ForeignKey(SearchEngines, null=True)
    variable_name = models.CharField(null=False, max_length=255, db_index=True)
    variable_description = models.CharField(null=True, max_length=1000)
    deprecated_luv_variable = models.BooleanField(default=False, null=False)
    fk_luv_user_created = models.ForeignKey(User, related_name='fk_luv_user_created', null=True)
    fk_luv_user_updated = models.ForeignKey(User, related_name='fk_luv_user_updated', null=True)
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=False, editable=False)

    def save(self):
        if not self.pk_lookupvariables_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()


class LookUps(models.Model):
    pk_lookups_id = models.AutoField(null=False, primary_key=True, editable=False)
    fk_lookupvariables = models.ForeignKey(LookUpVariables, null=True)
    # TODO: make sure any calls to this account for a no display_name error
    display_name = models.CharField(null=True, max_length=255)
    url_variable = models.CharField(null=False, max_length=255, db_index=True)
    deprecated_lu_variable = models.BooleanField(default=False, null=False)
    fk_lu_user_created = models.ForeignKey(User, related_name='fk_lu_user_created', null=True)
    fk_lu_user_updated = models.ForeignKey(User, related_name='fk_lu_user_updated', null=True)
    date_created = models.DateTimeField(null=False, editable=False)
    date_updated = models.DateTimeField(null=False, editable=False)

    def save(self):
        if not self.pk_lookups_id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()

