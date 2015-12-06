from django import forms
from .models import SearchEngines

class NewProjectForm(forms.Form):
    # TODO: Include resolution to grab user information for logging!!!
    project_name = forms.CharField(label='Project Name', max_length=255, min_length=5)
    project_decription = forms.CharField(label='Project Description', max_length=8000)
    project_search_engine = forms.ModelChoiceField(queryset=SearchEngines.objects.all())