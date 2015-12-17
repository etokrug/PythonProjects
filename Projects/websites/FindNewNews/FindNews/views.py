from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from .models import SearchEngines, Project
from .forms import NewProjectForm

def customsearch(request):
    return HttpResponse("Custom Search Placeholder")

def createproject(request):
    if request.method == 'POST':
        # search_engines = SearchEngines.objects.all()
        form = NewProjectForm(request.POST)
        if form.is_valid():
            # pName = form.save()
            test = form.cleaned_data
            projName = test.get('project_name')
            pForm, created = Project.objects.get_or_create(project_name=projName)
            if created:
                # HttpResponseRedirect('/Submitted/')
                print("Submission PASSED")
                submitted(request)
            else:
                # HttpResponse('/SubmissionFailed/')
                print("Submission FAILED")
                submissionfailed(request)
    # context = RequestContext(request, {'search_engines': search_engines,})
    else:
        form = NewProjectForm()
        print("Else block - New form")
        return render(request, 'FindNews/createproject.html', {'form': form})


def submitted(request): # TODO: Create one template that takes the bool created from the createproject template boi
    return render(request, 'FindNews/submitted.html')


def submissionfailed(request):
    return render(request, 'FindNews/submissionfailed.html')