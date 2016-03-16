from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
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
                # TODO: Get user credentials and pass here.
                projDesc = test.get('project_description')
                messages.add_message(request, messages.SUCCESS, 'Thanks for creating a project!')
            return submitted(request, created)
    # context = RequestContext(request, {'search_engines': search_engines,})
    else:
        form = NewProjectForm()
        print("Else block - New form")
        return render(request, 'FindNews/createproject.html', {'form': form, 'current_user':request.user.username})


def submitted(request, created):
    if created:
        title = 'Entry Submitted'
        message = 'Entry did not exist in system and was created'
    else:
        title = 'Entry Failed'
        message = 'Entry already in system - Submission Failed'
    return render(request, 'FindNews/submitted.html', {'title':title, 'message':message, 'current_user':request.user.username})


