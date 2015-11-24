from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    fk_user_id = models.ForeignKey(User)
    project_name = models.CharField(max_length=255)
    project_description = models.CharField(max_length=8000)
    date_created = models.DateTimeField
