from django.contrib import admin

from .models import Project, SearchEngines, ProjectSearches, LinkUrls, SearchResults, LookUpVariables, LookUps

admin.site.register(Project)
admin.site.register(SearchEngines)
admin.site.register(ProjectSearches)
admin.site.register(LinkUrls)
admin.site.register(SearchResults)
admin.site.register(LookUpVariables)
admin.site.register(LookUps)

