from django.forms import Form, ModelForm, Textarea, TextInput
from .models import SearchEngines, Project

class NewProjectForm(ModelForm):
    # TODO: Include resolution to grab user information for logging!!!
    class Meta:
        model = Project
        fields = ['project_name', 'project_description']
        labels = {
            'project_name': 'Project Name',
        }
        widgets = {
            'project_description': Textarea(attrs={
                'rows': 8,
                'cols': 40,
            }),
        }