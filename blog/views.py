from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_view(request):
  template = loader.get_template('home.html')
  user = request.user
  context = {
        'user': user
    }
  return HttpResponse(template.render(context, request))
