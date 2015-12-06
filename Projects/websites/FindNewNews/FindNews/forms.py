from django.forms import Form, ModelForm, Textarea, TextInput
from .models import SearchEngines, Project

class NewProjectForm(ModelForm):
    # TODO: Include resolution to grab user information for logging!!!
    class Meta:
        model = Project
        fields = ['project_name', 'project_description']
        widgets = {
            'project_description': Textarea(),
        }
    #PNAME = 'Project Name:'
    #PDESC = 'Project Description: '
    #PSEARCHENG = 'Project Search Engine: '
    #project_name = forms.CharField(label='Project Name', max_length=255, min_length=5)
    #project_decription = forms.CharField(label='Project Description', widget=forms.Textarea, max_length=8000)
    #project_search_engine = forms.ModelChoiceField(queryset=SearchEngines.objects.all())