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
            pName = form.save()
            HttpResponseRedirect('/Submitted/')
            print("If block, saved")
    # context = RequestContext(request, {'search_engines': search_engines,})
    else:
        form = NewProjectForm()
        print("Else block - New form")
    return render(request, 'FindNews/createproject.html', {'form': form})

def submitted(request):
    return render(request, 'FindNews/submitted.html')

