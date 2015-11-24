from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Project(models.Model):
    pk_project_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(User)
    project_name = models.CharField(max_length=255)
    project_description = models.CharField(max_length=8000)
    date_created = models.DateTimeField

    #Reference
    #http://www.b-list.org/weblog/2006/nov/02/django-tips-auto-populated-fields/

    # TODO: Build this model like whoa
