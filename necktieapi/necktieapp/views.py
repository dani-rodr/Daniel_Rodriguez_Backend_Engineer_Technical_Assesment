from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

from necktieapp.models import Doctor
from necktieapp.doctorgenerator import DoctorGenerator

# Create your views here.

def index(request):
    return HttpResponse(json.dumps([{'message':'Welcome'}]), content_type='text/json')

def get_all_doctors(request):
    if request.method != 'GET':
        emptyResponse = json.dumps([{}])
        return HttpResponse(emptyResponse, content_type='text/json')
        
    emptyResponse = json.dumps([{}])
    return HttpResponse(emptyResponse, content_type='text/json')
    
def generate_doctor_data(request):
    # Doctor.objects.all().delete()

    generator = DoctorGenerator()
    generator.generate()
    doctors = serializers.serialize('json', Doctor.objects.all())

    return HttpResponse(json.loads(doctors), content_type='application/json')
