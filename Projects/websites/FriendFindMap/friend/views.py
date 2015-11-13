from django.http import HttpResponse
from django.template import RequestContext, loader


def friend(request):
    template = loader.get_template('friend/loginpage.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
