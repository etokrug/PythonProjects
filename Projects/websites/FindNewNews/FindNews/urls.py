from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^CustomSearch/$', views.customsearch, name='customsearch'),
    url(r'^CreateProject/$', views.createproject, name='createproject'),
    url(r'^Submitted/$', views.submitted, name='submitted'),
    url(r'^SubmissionFailed/$', views.submissionfailed, name='submissionfailed')
]
