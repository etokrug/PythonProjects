from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def customsearch(request):
    return HttpResponse("Custom Search Placeholder")

def createproject(request):
    return HttpResponse("Create Project Holder")

