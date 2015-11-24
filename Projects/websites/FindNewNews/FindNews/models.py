from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Project(models.Model):
    pk_project_id = models.AutoField(null=False, primary_key=True)
    fk_user_id = models.ForeignKey(User, null=False)
    project_name = models.CharField(null=False, max_length=255)
    project_description = models.CharField(max_length=8000)
    date_created = models.DateTimeField(null=False)

    # TODO: def createNewProject(args..)
    #Reference
    #http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/

class SearchEngines(models.Model):
    pk_searchengines_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(User)
    # The name given to this search either on the site OR just for these purposes
    search_name = models.CharField(null=False, max_length=150)
    # This would be like "google.com"
    search_site = models.CharField(null=False, max_length=300)
    # This would be the api used like google custom search/google site search/bing etc
    search_api = models.CharField(max_length=300)
    # The key needed/issued to access the api
    search_key = models.CharField(max_length=300)
    # The api key if you need to register an app with the site
    api_key = models.CharField(max_length=300)



class ProjectSearches(models.Model):
    pk_projectsearches_id = models.AutoField(null=False, primary_key=True)
    fk_project_id = models.ForeignKey(Project, null=False)

