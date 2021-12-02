from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

def index(request):
    return HttpResponse(json.dumps([{'message':'Welcome'}]), content_type='text/json')

def get_all_doctors(request):
    if request.method != 'GET':
        emptyResponse = json.dumps([{}])
        return HttpResponse(emptyResponse, content_type='text/json')
        
    emptyResponse = json.dumps([{}])
    return HttpResponse(emptyResponse, content_type='text/json')
    
