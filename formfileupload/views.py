from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from lib.storage import azure_utils

def index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context, request))

def signature(request):
    result = azure_utils.generate_access_signature(request.post.file)
    return HttpResponse(result)