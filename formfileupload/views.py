from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from lib.storage.azure_utils import AzureUtils
from django.conf import settings
import json
import urlparse

def index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context, request))

def signature(request, file_name):
    azure_utils = AzureUtils(settings.AZURE_ACCOUNT_NAME, settings.AZURE_ACCOUNT_KEY)
    signature = azure_utils.generate_access_signature(file_name)
    result = {
        "bloburl": urlparse.urljoin("https://tempodevelop.blob.core.windows.net/tmp/", file_name),
        "signature": signature,
    }   
    return HttpResponse(json.dumps(result))