from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import SearchEngines, Project


def customsearch(request):
    return HttpResponse("Custom Search Placeholder")

def createproject(request):
    search_engines = SearchEngines.objects.all()
    context = RequestContext(request, {'search_engines': search_engines,})
    return render(request, 'FindNews/createproject.html', context)

